#!/usr/bin/python3
import matplotlib.pyplot as plt
import numpy as np
from matplotlib import cm


def plottwosets(data_set_1, data_set_2, title):
    data_set_1 = np.array(data_set_1)
    data_set_2 = np.array(data_set_2)

    plt.plot(data_set_1[0], data_set_1[1], 'r', data_set_2[0], data_set_2[1], 'b')

    plt.xlim(0, 1340)
    plt.ylim(min(min(data_set_1[1]), min(data_set_2[1])), max(max(data_set_1[1]), max(data_set_2[1])))
    plt.title(title)
    plt.xlabel('Raman Shift (Wavenumbers)')
    plt.ylabel('Intensity')
    plt.show()


def plot_example():
    # Edit me!
    file_name = 'data/20180702 50 mcg mL Myoglobin S1R1.txt'
    emission = np.arange(200, 802, 2)
    excitation = np.arange(200, 504, 4)
    title = '50 mcg/mL Myoglobin'

    # Leave me alone
    levels = (range(0, 2000000, 50000))
    cmap = cm.nipy_spectral


plot_example()
