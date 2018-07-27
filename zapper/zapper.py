#!/usr/local/bin/python
import csv
import numpy as np
import os
import scipy.stats as stats
from remline.remline import remove_line_dir
from plotting.ramanplots.tworamanspectra import plottwosets


def data_extract(input_dir, file_name, x_length):
    data = [[0 for rows in range(x_length)] for cols in range(2)]
    with open(input_dir + file_name, 'r') as read_file:
        data_reader = csv.reader(read_file, delimiter='\t')
        row_count = 0
        for row in data_reader:
            column_count = 0
            for column in row:
                try:
                    data[column_count][row_count] = column
                except IndexError:
                    pass
                column_count += 1
            row_count += 1
    read_file.close()
    return data


def zap_dir(factor, working_dir):
    remove_line_dir(working_dir)
    working_dir = working_dir + 'Shortened/'
    source_files = os.listdir(working_dir)

    if not os.path.exists(working_dir + 'Zapped/'):
        os.mkdir(working_dir + 'Zapped/')
    output_dir = working_dir + 'Zapped/'

    data_sets = []
    for file in source_files:
        try:
            if file[:-6] not in data_sets and file[-7] is not '_':
                data_sets.append(file[:-6])
        except IndexError:
            pass

    for data_set in data_sets:
        for working_file in source_files:
            print('Zapping file ', working_file)
            zapped_data = [[0 for rows in range(0, 1340, 1)] for cols in range(2)]
            set_zapped_wave = True
            if str(data_set) in str(working_file):
                working_data = data_extract(working_dir, working_file, 1340)
                for reference_file in source_files:
                    if str(data_set) in str(reference_file):
                        reference_data = data_extract(working_dir, reference_file, 1340)
                        column_count = 0
                        for column in working_data:
                            if column_count is 1:
                                break
                            row_count = 0
                            for row in column:
                                if row == reference_data[0][row_count]:
                                    if set_zapped_wave:
                                        zapped_data[0][row_count] = reference_data[0][row_count]
                                    if (1 - factor) * float(working_data[1][row_count]) <= \
                                            float(reference_data[1][row_count]) <= \
                                            (1 + factor) * float(working_data[1][row_count]):
                                        zapped_data[1][row_count] = working_data[1][row_count]
                                    else:
                                        xrange = []
                                        for x in range(row_count - 3, row_count + 4, 1):
                                            try:
                                                xrange.append(x)
                                            except IndexError:
                                                pass
                                        ydata = []
                                        try:
                                            for x in xrange:
                                                ydata.append(float(working_data[1][x]))

                                            slope, intercept, r_value, p_value, std_err = stats.linregress(xrange, ydata)
                                            zapped_data[1][row_count] = slope * row_count + intercept
                                        except IndexError:
                                            pass
                                    row_count += 1

                            set_zapped_wave = False
                            column_count += 1
                output_file_name = working_file[:-4] + 'z' + working_file[-4:]
                output_file = open(working_dir + '/Zapped/' + output_file_name, 'w')
                zapped_data = np.transpose(zapped_data)
                for row in zapped_data:
                    output_file.write('%s\t%s\n' % (row[0], row[1]))
                output_file.close()
                # plottwosets(working_data, np.transpose(zapped_data), working_file)


def zap_oxygen(input_file_name):
    # TODO: zap the oxygen Raman band using a linear interpolation between the start and end points
    wave_start = 1600
    wave_end = 1700

    # slope, intecept = stats.linregress(x, y)

    for data in range(wave_start, wave_end):
        pass


zap_dir(0.25, 'D:/OneDrive - University of Pittsburgh/Xenon Binding Project Shared Folder/204 nm Raman Data/20180718 Myoglobin Tests/')
