#!/usr/bin/python3
import matplotlib.pyplot as plt
import numpy as np
from matplotlib import cm


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
