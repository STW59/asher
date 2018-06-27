#!/usr/bin/python3
import matplotlib.pyplot as plt
import numpy as np
from matplotlib import cm

myoglobin = np.loadtxt('20180626 Myo2DSqud1.txt', delimiter='\t')
myoglobin_transpose = np.transpose(myoglobin)
x = np.arange(200, 802, 2)
y = np.arange(200, 804, 4)

levels = (0, 2000, 4000, 6000, 8000, 10000, 15000, 20000, 30000, 40000, 50000, 60000, 70000, 80000)
norm = cm.colors.Normalize(vmax=abs(myoglobin_transpose).max(), vmin=0)
cmap = cm.afmhot

# contour the gridded data, plotting dots at the nonuniform data points.
plt.contourf(x, y, myoglobin_transpose, levels, cmap=cm.get_cmap(cmap, levels))
plt.colorbar()  # draw colorbar

# plot data points.
plt.xlim(200, 800)
plt.ylim(200, 800)
plt.axis('equal')
plt.title('25 mcg/mL Myoglobin 2D Fluorescence')
plt.xlabel('Emission Wavelength (nm)')
plt.ylabel('Excitation Wavelength (nm)')
plt.show()
