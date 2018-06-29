#!/usr/bin/python3
import csv
import matplotlib.pyplot as plt
import numpy as np
from matplotlib import cm


def fluorescence_plot():
    # Import data
    file_name = '20180629 50 mcg mL Myoglobin S1R1 Run 2.txt'
    emission = np.arange(200, 802, 2)
    excitation = np.arange(200, 504, 4)

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

    myoglobin_array = np.array(myoglobin)

    # Plot data
    # levels = (0, 2000, 4000, 6000, 8000, 10000, 15000, 20000, 30000, 40000, 50000, 60000, 70000, 80000)
    # levels = 30
    levels = (range(0, 2000000, 50000))
    # norm = cm.colors.Normalize(vmax=abs(myoglobin_array).max(), vmin=0)
    cmap = cm.nipy_spectral

    # contour the gridded data, plotting dots at the nonuniform data points.
    plt.contourf(emission, excitation, myoglobin, levels, cmap=cm.get_cmap(cmap, levels))
    plt.colorbar()  # draw colorbar

    # plot data points.
    plt.xlim(200, 800)
    plt.ylim(200, 500)
    plt.axis('equal')
    # plt.title(file_name)
    plt.xlabel('Emission Wavelength (nm)')
    plt.ylabel('Excitation Wavelength (nm)')
    plt.show()


def main():
    fluorescence_plot()


main()
