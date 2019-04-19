""" Module alazar
A module for reading and processing alazar data"""

import numpy as np
from ROOT import TFile

# getting data
def root2np(tfile, tgraph):
    """ Converts ROOT data to numpy"""
    data = TFile(tfile).Get(tgraph) 
    # From Root array to numpy array
    # see https://gist.github.com/jepio/4802f87164f20e266503
    x_data = np.array(data.GetX(), copy=True)
    y_data = np.array(data.GetY(), copy=True)
    data = np.vstack((x_data, y_data))
    return data


# fft data
def fft_timeline(x_data, y_data, samples=1):
    binning = abs(x_data[0]-x_data[1])
    total_entries = x_data.size
    samples = samples
    sample_entries = total_entries / samples
    print "total entries", total_entries, "with binning [s]", binning, "and duration [s]", binning * sample_entries
    print "samples:", samples, "with duration [s]", binning * sample_entries

    # create arrays
    frequency = np.fft.fftfreq(sample_entries, binning) 
    # make it real and zero!
    voltage = np.abs(np.fft.fft(y_data[0:sample_entries])) * 0.0

    # sampling and averaging
    for index in range(samples):
        voltage_data = y_data[index*sample_entries:(index+1)*sample_entries]
        # TODO: normalization?! --> integral
        voltage = voltage + np.abs(np.fft.fft(voltage_data)) / sample_entries
        #print "no", index
    voltage = voltage / samples
    return frequency[frequency>=0], voltage[frequency>=0]
