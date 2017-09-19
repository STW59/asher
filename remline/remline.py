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

MAX_LENGTH = 1340


def remove_line_dir(path):
    """This function is designed to remove any lines past the designated MAX_LENGTH in a given spectrum file for all
    files in a given directory.

        Args:
            path (str): This is the file path to where the spectrum files are stored.
    """

    print("Input path: {}".format(path))

    file_count = 0

    source_files = os.listdir(path)

    if not os.path.exists(path + 'Shortened/'):
        os.mkdir(path + 'Shortened/')

    for filename in source_files:
        if '.prn' in filename:
            file_count += 1

            f = open(path + filename, 'r')
            w = open(path + 'Shortened/' + filename, 'w')

            line_count = 0

            for line in f:
                line_count += 1
                if line_count < MAX_LENGTH:
                    w.write(line)
                elif line_count == MAX_LENGTH:
                    w.write(line.rstrip())

            f.close()
            w.close()

    print('Processed files = {}'.format(file_count))


def remove_line(file_set, num_files, input_dir, output_dir):
    """This function is designed to remove any lines past the designated MAX_LENGTH in a given spectrum file.

    Args:
        file_set (str): This is the name of the set of files before the number and extension.
        num_files (int): This is the number of files in the spectral set.
        input_dir (str): This is the input directory for the files being processed.
        output_dir (str): This is the output directory for the files.
    """

    print('Processing file set {}'.format(file_set))

    file_count = 0

    for i in range(1, num_files+1):
        f = open(input_dir + file_set + '_{}.prn'.format(i), 'r')
        w = open(output_dir + file_set + '_T_{}.prn'.format(i), 'w')

        line_count = 0

        for line in f:
            line_count += 1
            if line_count < MAX_LENGTH:
                w.write(line)
            elif line_count == MAX_LENGTH:
                w.write(line.rstrip())

        f.close()
        w.close()
        file_count += 1

    print('Files processed: {}'.format(file_count))


def main():
    # remove_line('D2O_3min_10spc', 10, 'E:/Spectroscopy Group/Stephen/Test Data/', 'E:/Spectroscopy Group/Stephen/Test Data/Shortened/')

    remove_line_dir('E:/Spectroscopy Group/2017-08-17 Q20 Fibrils 37C/')

main()
