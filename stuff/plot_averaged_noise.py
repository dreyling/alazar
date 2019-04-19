import math 
import sys
import numpy as np
import matplotlib.pyplot as plt
import inspect, os


filename = sys.argv[1]
frequency, Voltage = np.loadtxt(filename)


plt.plot(frequency, Voltage)
plt.xscale('log')
plt.yscale('log')

output_name = sys.argv[0][:-3] + sys.argv[1] + '.pdf' 
plt.savefig(output_name)
print "evince " + output_name + ' &' 
#plt.show()
