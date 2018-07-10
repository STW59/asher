#!/usr/bin/python3
import csv
import matplotlib.pyplot as plt
import numpy as np
from matplotlib import cm


# Leave me alone!
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
    read_file.close()
    return data


# Leave me alone!
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


# Leave me alone!
def plot2d(levels, cmap, emission, excitation, data, title):
    data_set = np.array(data)
    plt.contourf(emission, excitation, data_set, levels, cmap=cm.get_cmap(cmap, levels))
    plt.colorbar()

    plt.xlim(min(emission), max(emission) - 2)
    plt.ylim(min(excitation), max(excitation) - 4)
    plt.axis('equal')
    plt.title(title)
    plt.xlabel('Emission Wavelength (nm)')
    plt.ylabel('Excitation Wavelength (nm)')
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

    plot_data = data_extract(file_name, emission, excitation)
    plot2d(levels, cmap, emission, excitation, plot_data, title)


def subtract_example():
    # Edit me!
    file_1_name = 'data/20180703 3 mcg mL Myoglobin vacuumed S1R1.txt'
    file_2_name = 'data/20180705 3 mcg mL Myoglobin Xe S1R1.txt'
    emission = np.arange(200, 488, 2)
    excitation = np.arange(200, 356, 4)
    title = '3 mcg/mL Myo - Myo Xe'

    # Leave me alone!
    levels = list(range(-800000, 800000, 50000))
    cmap = cm.bwr

    myoglobin_1 = data_extract(file_1_name, emission, excitation)
    myoglobin_2 = data_extract(file_2_name, emission, excitation)

    myoglobin_data = fluorescence_subtract(myoglobin_1, myoglobin_2, emission, excitation)
    plot2d(levels, cmap, emission, excitation, myoglobin_data, title)


# Put a "# " in front of the one you DON'T want to run
plot_example()
# subtract_example()
