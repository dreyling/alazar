'''read and analyze Alazar root files

Usage:
    read_root_file.py (--configuration=<configuration>)

Options:
    --configuration=<configuration> yaml file [required]
    -h --help                   show usage of this script
    -v --version                show the version of this script
'''

import yaml
from docopt import docopt
import numpy as np
import sys

import matplotlib.pyplot as plt
#import matplotlib.gridspec as gridspec
#from scipy.optimize import curve_fit

from ROOT import TFile

############################################
# arguments
arguments = docopt(__doc__, version='read and analyze Alazar root files')
configuration = yaml.load(open(arguments['--configuration']))
#print configuration['root_file']

############################################
# getting data
data = TFile(configuration['root_file']).Get('Data of channel ChA') 
#print data

# From Root array to numpy array
# see https://gist.github.com/jepio/4802f87164f20e266503
x_data = np.array(data.GetX(), copy=True)
y_data = np.array(data.GetY(), copy=True)
#print x_data, y_data
#print len(x_data), len(y_data)


################################################
# sampling for spectrum

binning = abs(x_data[0]-x_data[1])
total_size = x_data.size
samples = 1000
sample_size = total_size / samples
print "samples", samples, "binning", binning, "duration", binning * sample_size, "sample size", sample_size

frequency = np.fft.fftfreq(sample_size, binning) 
voltage = np.fft.fft(y_data[0:sample_size]) / sample_size
# make it real and zero!
voltage = np.abs(voltage) * 0.0

# sampling and averaging
for index in range(samples):
    voltage_data = y_data[index*sample_size:(index+1)*sample_size]
    voltage = voltage + np.abs(np.fft.fft(voltage_data)) / sample_size
    print "no", index
voltage = voltage / samples


############################################
# plotting
fig, ax = plt.subplots(figsize=(5, 3))#, dpi=100)
fig.subplots_adjust(left=0.20, right=0.97, top=0.97, bottom=0.20)

ax.plot(frequency, voltage)

ax.set_xscale('log')
ax.set_yscale('log')
ax.set_xlabel('frequency')
ax.set_ylabel('signal [V]')

# save 
title_save = sys.argv[0][:-3]
name_save =  "output/" + title_save + str(".pdf") 
fig.savefig(name_save)
print "evince " + name_save + "&"




exit()




np.savetxt('total_' + folder_name + '_' + stop, (frequency, Voltage), fmt='%1.4e') 



