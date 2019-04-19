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
import alazar

import matplotlib.pyplot as plt
#import matplotlib.gridspec as gridspec
#from scipy.optimize import curve_fit

# arguments
arguments = docopt(__doc__, version='read and analyze Alazar root files')
configuration = yaml.load(open(arguments['--configuration']))
#print configuration['root_file']

# getting data
data = alazar.root2np(configuration['root_tfile'], configuration['root_tgraph']) 
x_data = data[0]
y_data = data[1]

for index in [1, 100, 10000]: 
    # sampling for spectrum
    #frequency, voltage = alazar.fft_timeline(x_data, y_data, samples = configuration['fft_samples'])
    frequency, voltage = alazar.fft_timeline(x_data, y_data, index)

    # plotting
    fig, ax = plt.subplots(figsize=(5, 3))#, dpi=100)
    fig.subplots_adjust(left=0.20, right=0.97, top=0.97, bottom=0.20)
    ax.plot(frequency, voltage, label=str(index))
    
    ax.set_xscale('log')
    ax.set_yscale('log')
    ax.set_xlabel('frequency')
    ax.set_ylabel('signal [V]')
    ax.legend()

    # save 
    title_save = sys.argv[0][:-3]
    #name_save =  "output/" + title_save + "_" + str(configuration['fft_samples']) + str(".pdf") 
    name_save =  "output/" + title_save + "_" + str(index) + str(".pdf") 
    fig.savefig(name_save)
    print "evince " + name_save + "&"


exit()

np.savetxt('total_' + folder_name + '_' + stop, (frequency, Voltage), fmt='%1.4e') 
