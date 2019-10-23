#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Oct 20 16:33:49 2019

@author: codenics
"""
import numpy as np
import scipy.ndimage as snd
import NanoImagingPack as nip


def CosmicRAySim (anImage, NumShots = 500, ShotValue = 255):
    
    
    dirtyImage = anImage.copy()
    
    return dirtyImage

anImage = nip.readim()
dirtyImg = CosmicRaySim(anImage)
dirtyImg


def RemoveHotPixels (anImage, threshValue = 200, kernelSize = 3):
    
    #sp.signal.medfilt
    myMask = anImage > threshValue
    
    anImage[myMask] = filtered[mask]    
    
    return cleanImg;

catE(dirtyImg, RemoveHotPixels(dirtyImg), anImage)