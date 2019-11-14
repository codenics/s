#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov 13 18:56:09 2019
Exercise 2
@author: Darko Gilbert 
"""

import numpy as np
import NanoImagingPack as nip
import matplotlib.pyplot as plt
from imageio import imread
from matplotlib.colors import ListedColormap
import matplotlib as mpl

#Task 1
cdict = {'red':   [[0.0,  0.0, 0.0],
                   [0.5,  1.0, 1.0],
                   [1.0,  1.0, 1.0]],
         'green': [[0.0,  0.0, 0.0],
                   [0.25, 0.0, 0.0],
                   [0.75, 1.0, 1.0],
                   [1.0,  1.0, 1.0]],
         'blue':  [[0.0,  0.0, 0.0],
                   [0.5,  0.0, 0.0],
                   [1.0,  1.0, 1.0]]}


def plot_linearmap(cdict):
    newcmp = LinearSegmentedColormap('testCmap', segmentdata=cdict, N=256)
    rgba = newcmp(np.linspace(0, 1, 256))
    rgba = np.sin(rgba)
    fig, ax = plt.subplots(figsize=(4, 3), constrained_layout=True)
    col = ['r', 'g', 'b']
    for xx in [0.25, 0.5, 0.75]:
        ax.axvline(xx, color='0.7', linestyle='--')
    for i in range(3):
        ax.plot(np.arange(256)/256, rgba[:, i], color=col[i])
    ax.set_xlabel('index')
    ax.set_ylabel('RGB')
    plt.show()

plot_linearmap(cdict)
"""
N = 256
vals = np.ones((N, 4))
vals[:, 0] = np.linspace(90/256, 1, N)
vals[:, 1] = np.linspace(39/256, 1, N)
vals[:, 2] = np.linspace(1-(90/256 + 39/256), 1, N)
rgbcmap = ListedColormap(vals)

figure, (ax1, ax2) = plt.subplots(1, 2, figsize=(8, 5))
img = imread('nice_img.jpg')
rgbcmapseg = mpl.colors.LinearSegmentedColormap.from_list('custom', 
                                             [(0,    'red'),
                                              (0.5, 'green'),
                                              (1,    'blue')], N=126)

ax1.imshow(img, cmap=rgbcmapseg)

norm = mpl.colors.Normalize(vmin=2, vmax=10)
mpl.colorbar.ColorbarBase(ax2, cmap=rgbcmapseg, norm=norm)
plt.show()

"""
#Task 3
R = 10
orka = nip.readim('orka')

apsf = nip.rr(orka.shape)<R
apsf_ft = nip.ft(apsf)
apsf_ift = nip.ift(apsf_ft)
apsf_abs_square = np.square(np.abs(apsf_ift))

orka_ft = nip.ft(orka)

convolve = orka_ft*apsf_abs_square

finalImage = np.real(nip.ift(convolve))

figure, (ax1, ax2) = plt.subplots(1, 2)
ax1.set_title('original')
ax2.set_title('after convolution')

ax1.imshow(orka)
ax2.imshow(finalImage)
figure




