#!/usr/bin/python3
import csv
import matplotlib.pyplot as plt
import numpy as np
from matplotlib import cm


def fluorescence_subtract():
    # Import data
    file_1_name = '20180629 50 mcg mL Myoglobin S1R1.txt'
    file_2_name = '20180629 50 mcg mL Myoglobin S1R1 Run 2.txt'

    emission = np.arange(200, 802, 2)
    excitation = np.arange(200, 504, 4)

    myoglobin_1 = [[0 for setrow in range(len(emission))] for setcol in range(len(excitation))]
    with open(file_1_name, 'r') as read_file:
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
                            myoglobin_1[column_count - 2][row_count - 3] = column
                        except IndexError:
                            pass
    read_file.close()

    myoglobin_2 = [[0 for setrow in range(len(emission))] for setcol in range(len(excitation))]
    with open(file_2_name, 'r') as read_file:
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
                            myoglobin_2[column_count - 2][row_count - 3] = column
                        except IndexError:
                            pass
    read_file.close()

    myoglobin_sub = [[0 for setrow in range(len(emission))] for setcol in range(len(excitation))]
    row_count = 0
    for line in myoglobin_1:
        column_count = 0
        for column in line:
            subtracted_value = float(myoglobin_1[row_count][column_count]) - float(myoglobin_2[row_count][column_count])
            myoglobin_sub[row_count][column_count] = subtracted_value
            column_count += 1
        row_count += 1
    myoglobin_sub_array = np.array(myoglobin_sub)

    # Plot data
    levels = list(range(-2000000, 2000000, 50000))

    cmap = cm.bwr

    # contour the gridded data, plotting dots at the nonuniform data points.
    plt.contourf(emission, excitation, myoglobin_sub_array, levels, cmap=cm.get_cmap(cmap, levels))
    plt.colorbar()  # draw colorbar

    # plot data points.
    plt.xlim(200, 800)
    plt.ylim(200, 500)
    plt.axis('equal')
    plt.title('Subtracted Spectrum')
    plt.xlabel('Emission Wavelength (nm)')
    plt.ylabel('Excitation Wavelength (nm)')
    plt.show()


def main():
    fluorescence_subtract()


main()
