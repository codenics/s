#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov 13 18:56:09 2019
Exercise 2
@author: Darko Gilbert 
"""

#Task1
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
import matplotlib.cm as cm
from matplotlib.colors import ListedColormap 
import imageio as img
import NanoImagingPack as nip

imag = img.imread('nice_img.jpg')
N = 360
deg = np.arange(0, N)
blue = (np.sin((deg/N)*2*np.pi)+1)*0.5
green = np.roll(blue, 120)
red = np.roll(green, 120 )

vals = np.ones((N, 4))
vals[:, 0] = red
vals[:, 1] = green
vals[:, 2] = blue
newcolormap = ListedColormap(vals)
plt.plot(deg, green, deg, red, deg, blue)
plt.show()

plt.imshow(imag, cmap=newcolormap)
plt.colorbar()
plt.show()

plt.imshow(imag, cmap='viridis')
plt.colorbar()

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




