#!/usr/bin/python3
import os


def main():
    separate_jobs('D:/OneDrive - University of Pittsburgh/Asher Lab/Lab Stuff/Phi Angle/Computation/A2/Vibrations/')


def separate_jobs(path):
    print("Input path: {}".format(path))

    input_file_count = 0
    output_file_count = 0

    source_files = os.listdir(path)

    if not os.path.exists(path + 'Separated/'):
        os.mkdir(path + 'Separated/')

    for filename in source_files:
        if '.out' in filename:
            input_file_count += 1

            f = open(path + filename, 'r')

            # TODO: read input
            for line in f:
                if line.startswith(' Initial command'):
                    print(line)
                elif line.startswith(' Normal termination'):
                    print(line)

            # TODO: write output files

            f.close()

    print('Input files processed = {}'.format(input_file_count))
    print('Output files created = {}'.format(output_file_count))


main()
