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
import sys
import alazar

import matplotlib.pyplot as plt

# arguments
arguments = docopt(__doc__, version='read and analyze Alazar root files')
configuration = yaml.load(open(arguments['--configuration']))

# getting data
data = alazar.root2np(configuration['root_tfile'], configuration['root_tgraph']) 

# plotting
fig, ax = plt.subplots(figsize=(5, 3))#, dpi=100)
fig.subplots_adjust(left=0.20, right=0.97, top=0.97, bottom=0.20)

ax.plot(data[0], data[1])

ax.set_xlabel('time [s]')
ax.set_ylabel('signal [V]')

# save 
title_save = sys.argv[0][:-3]
name_save =  "output/" + title_save + str(".pdf") 
fig.savefig(name_save)
print "evince " + name_save + "&"

