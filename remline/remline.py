'''
This program is designed to remove any lines past the designated MAX_LENGTH in a given spectrum file.
Written by Stephen E. White
Last edited 05JUN2017
'''

# TODO: Turn into a class so it can be called from other files.
# TODO: Write a dir input so that all files in the dir can be edited.

MAX_LENGTH = 1340


def remove_line(file_set, num_files):
    """This function is designed to remove any lines past the designated MAX_LENGTH in a given spectrum file.
    Note: this program currently works only if the files being processed are in the same directory as the .py file.

    Args:
        file_set (str): This is the name of the set of files before the number and extension.
        num_files (int): THis is the number of files in the spectral set.
    """

    print('Processing file set {}'.format(file_set))

    for i in range(1, num_files+1):
        f = open(file_set + '_{}.prn'.format(i), 'r')
        w = open(file_set + '_{}_T.prn'.format(i), 'w')

        line_count = 0

        for line in f:
            line_count += 1
            if line_count < MAX_LENGTH:
                w.write(line)
            elif line_count == MAX_LENGTH:
                w.write(line.rstrip())
            else:
                None

        f.close()
        w.close()


def main():
    # Program each file set here. Then run! All file sets programmed will be modified.
    remove_line('Cyclohexane-3sec-5spc', 5)
    remove_line('Cyclohexane_End-3sec-5spc', 5)
    remove_line('D2O_3min_10spc', 10)
    remove_line('Glutamine_D20_1mM_3min_10spc', 10)
    remove_line('Glutamine_D20_10mM_3min_10spc', 10)
    remove_line('Glutamine_D20_30mM_3min_10spc', 10)
    remove_line('NMR-3min-10spc', 10)

main()
