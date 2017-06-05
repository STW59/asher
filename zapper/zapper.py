# TODO: Delete the last row of the data files if greater than 1340
def zapper(inFile, reference, factor, window, numFiles):
    refSpectFile = open(reference, 'r')

    refSpectFile.close()


def lastRow(fileName):
    f = open(fileName, 'r')
    count = 0

    for line in f:
        count += 1

    if count > 1340:
        pass


def main():
    None

main()
