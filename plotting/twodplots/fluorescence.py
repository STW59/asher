#!/usr/bin/python3
import csv
import matplotlib.pyplot as plt
import numpy as np
from matplotlib import cm


def data_extract(file_name, emission, excitation):
    data = [[0 for setrow in range(len(emission))] for setcol in range(len(excitation))]
    with open(file_name, 'r') as read_file:
        data_reader = csv.reader(read_file, delimiter='\t')
        row_count = 0
        for row in data_reader:
            row_count += 1
            if row_count not in (1, 2):
                column_count = 0
                for column in row:
                    column_count += 1
                    if column_count is not 1:
                        try:
                            data[column_count - 2][row_count - 3] = column
                        except IndexError:
                            pass
    return data


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


def plot2d(levels, cmap, emission, excitation, data, title):
    data_set = np.array(data)
    plt.contourf(emission, excitation, data_set, levels, cmap=cm.get_cmap(cmap, levels))
    plt.colorbar()

    plt.xlim(200, 800)
    plt.ylim(200, 500)
    plt.axis('equal')
    plt.title(title)
    plt.xlabel('Emission Wavelength (nm)')
    plt.ylabel('Excitation Wavelength (nm)')
    plt.show()


def plot_example():
    file_name = 'data/20180628 Starna Cuvette S1R1.txt'
    emission = np.arange(200, 802, 2)
    excitation = np.arange(200, 504, 4)
    levels = (range(0, 2000000, 50000))
    cmap = cm.nipy_spectral
    title = 'Empty Starna Cuvette'

    plot_data = data_extract(file_name, emission, excitation)
    plot2d(levels, cmap, emission, excitation, plot_data, title)


def subtract_example():
    file_1_name = 'data/20180629 50 mcg mL Myoglobin S1R1.txt'
    file_2_name = 'data/20180629 50 mcg mL Myoglobin S1R1 Run 2.txt'
    emission = np.arange(200, 802, 2)
    excitation = np.arange(200, 504, 4)
    levels = list(range(-2000000, 2000000, 50000))
    cmap = cm.bwr
    title = 'Run 1 - Run 2'

    myoglobin_1 = data_extract(file_1_name, emission, excitation)
    myoglobin_2 = data_extract(file_2_name, emission, excitation)

    myoglobin_data = fluorescence_subtract(myoglobin_1, myoglobin_2, emission, excitation)
    plot2d(levels, cmap, emission, excitation, myoglobin_data, title)

# plot_example()
# subtract_example()
