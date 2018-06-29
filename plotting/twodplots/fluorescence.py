#!/usr/bin/python3
import csv
import numpy as np
from matplotlib import cm
from plotting.twodplots.plot2d import plot2d


def data_extract(file_name, emission, excitation):
    myoglobin = [[0 for setrow in range(len(emission))] for setcol in range(len(excitation))]
    with open(file_name, 'r') as read_file:
        myoglobin_reader = csv.reader(read_file, delimiter='\t')
        row_count = 0
        for row in myoglobin_reader:
            row_count += 1
            if row_count not in (1, 2):
                column_count = 0
                for column in row:
                    column_count += 1
                    if column_count is not 1:
                        try:
                            myoglobin[column_count - 2][row_count - 3] = column
                        except IndexError:
                            pass

    return myoglobin


def example():
    file_name = '20180628 Starna Cuvette S1R1.txt'
    emission = np.arange(200, 802, 2)
    excitation = np.arange(200, 504, 4)
    levels = (range(0, 2000000, 50000))
    cmap = cm.nipy_spectral
    title = 'Empty Starna Cuvette'

    plot_data = data_extract(file_name, emission, excitation)
    plot2d(levels, cmap, emission, excitation, plot_data, title)


# example()
