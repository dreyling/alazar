""" Module alazar
A module for reading and processing alazar data"""

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

def root2npz(root_file, root_tgraph_name):
    """ Converts ROOT data to numpy"""
    data = TFile(configuration[root_file]).Get(root_tgraph_name) 
    # From Root array to numpy array
    # see https://gist.github.com/jepio/4802f87164f20e266503
    x_data = np.array(data.GetX(), copy=True)
    y_data = np.array(data.GetY(), copy=True)
#print x_data, y_data
#print len(x_data), len(y_data)

############################################
# plotting
fig, ax = plt.subplots(figsize=(5, 3))#, dpi=100)
fig.subplots_adjust(left=0.20, right=0.97, top=0.97, bottom=0.20)

ax.plot(x_data, y_data)

ax.set_xlabel('time [s]')
ax.set_ylabel('signal [V]')

# save 
title_save = sys.argv[0][:-3]
name_save =  "output/" + title_save + str(".pdf") 
fig.savefig(name_save)
print "evince " + name_save + "&"

