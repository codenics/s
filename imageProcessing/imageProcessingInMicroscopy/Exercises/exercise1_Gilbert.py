#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 22 15:29:27 2019

@author: codenics
"""

import numpy as np
import scipy.ndimage as ndimg
import NanoImagingPack as nip

#Exercise 1, Task 1
def CosmicRaySim(anImage, NumShots=500, ShotValue=255):
    nrows, ncols = anImage.shape

    #Ensures that a particular set of random numbers is generate 
    #each run. In other words pass along random numbers.
    randState = np.random.RandomState(77)

    #Random numbers from 0 to 
    randPos = randState.randint(0, high=nrows*ncols, size=NumShots)
    dirtyImg = anImage.copy()
    #Flattes a copy of the original image and 
    #at Random Positions set their values to 0
    dirtyImg.flat[randPos] = 255
    
    dirtyImg = np.reshape(dirtyImg, anImage.shape)
    return dirtyImg


anImage = nip.readim()
dirtyImg = CosmicRaySim(anImage)
nip.v5(dirtyImg)
    





