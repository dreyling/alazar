import sys
import math
import numpy as np
import inspect, os

stop = sys.argv[1]

file_name = inspect.getfile(inspect.currentframe()) # script filename (usually with path)
folder_name = 'example_split'

data_path = folder_name 
files = os.listdir(data_path)
print len(files)

time, volt_data = np.loadtxt(data_path + '/' + 'x0000', delimiter='\t', usecols=(3, 4), unpack=True)
sample = time.size
binning = abs(time[0]-time[1])
print "sample", sample, "binning", binning, "duration", binning * sample

frequency = np.fft.fftfreq(sample, binning) 
Voltage = np.fft.fft(volt_data) / sample
# make it real and zero!
Voltage = np.abs(Voltage) * 0.0
print Voltage.size, "entries"
print "first entries:", Voltage[0:5]

for i, n in enumerate(files[:int(stop)]):
  time, volt_data = np.loadtxt(data_path + '/' + n, delimiter='\t', usecols=(3, 4), unpack=True)
  Voltage = Voltage + np.abs(np.fft.fft(volt_data)) / sample
  print "no", i
Voltage = Voltage / len(files[:int(stop)])
print Voltage.size, "entries"
print "first entries:", Voltage[0:5]

np.savetxt('total_' + folder_name + '_' + stop, (frequency, Voltage), fmt='%1.4e') 
