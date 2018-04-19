#!/usr/local/bin/python3

"""
This program is designed to remove any lines past the designated MAX_LENGTH in a given spectrum file.
Written by Stephen E. White

16JUN2017 - SEW
    Cleaned up some typos in the remove_line function.
    Edited remove_line function so that it takes the input and output directories as arguments so that the data no
        longer need to be in the same directory as the .py file.
    Added remove_line_dir function so that the user can specify a single directory and process all the files that end
        with a .prn file extension.

05JUN2017 - SEW
    Original File
"""

import os


def comma_change(path):
    """This function is designed to remove any lines past the designated MAX_LENGTH in a given spectrum file for all
    files in a given directory.

        Args:
            path (str): This is the file path to where the spectrum files are stored.
    """

    print("Input path: {}".format(path))

    file_count = 0

    source_files = os.listdir(path)

    if not os.path.exists(path + 'Tab/'):
        os.mkdir(path + 'Tab/')

    for filename in source_files:
        if '.prn' in filename:
            file_count += 1

            f = open(path + filename, 'r')
            w = open(path + '/Shortened/' + filename, 'w')

            for line in f:
                if ',' in line:
                    new_line = line.replace(',', '\t')
                else:
                    new_line = line
                w.write(new_line)

            f.close()
            w.close()

    print('Processed files = {}'.format(file_count))


def main():

    comma_change('D:/OneDrive - University of Pittsburgh/Asher Lab/Lab Stuff/DOSY Letter/20180419 NDQ20 UVRR 204 nm/')


main()
