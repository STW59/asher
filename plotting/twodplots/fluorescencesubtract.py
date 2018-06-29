#!/usr/bin/python3
import numpy as np
from matplotlib import cm
from plotting.twodplots.fluorescence import data_extract
from plotting.twodplots.plot2d import plot2d


def fluorescence_subtract(data_set_1, data_set_2, emission, excitation):
    data_sub = [[0 for setrow in range(len(emission))] for setcol in range(len(excitation))]
    row_count = 0
    for line in data_set_1:
        column_count = 0
        for column in line:
            subtracted_value = float(data_set_1[row_count][column_count]) - float(data_set_2[row_count][column_count])
            data_sub[row_count][column_count] = subtracted_value
            column_count += 1
        row_count += 1
    return data_sub


def example():
    file_1_name = '20180629 50 mcg mL Myoglobin S1R1.txt'
    file_2_name = '20180629 50 mcg mL Myoglobin S1R1 Run 2.txt'
    emission = np.arange(200, 802, 2)
    excitation = np.arange(200, 504, 4)
    levels = list(range(-2000000, 2000000, 50000))
    cmap = cm.bwr
    title = 'Run 1 - Run 2'

    myoglobin_1 = data_extract(file_1_name, emission, excitation)
    myoglobin_2 = data_extract(file_2_name, emission, excitation)

    myoglobin_data = fluorescence_subtract(myoglobin_1, myoglobin_2, emission, excitation)
    plot2d(levels, cmap, emission, excitation, myoglobin_data, title)


# example()
