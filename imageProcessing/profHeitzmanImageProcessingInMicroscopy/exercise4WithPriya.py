#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Dec  1 21:11:24 2019

@author: codenics
"""

import NanoImagingPack as nip
import numpy as np

def SimMicroscope(image, radius = 50, NPhotons = 100, stdv_gaussian = 5):
    image = nip.readim(image)
    pupil = nip.rr(image.shape) < radius
    h = nip.abssqr(nip.ift2d(pupil))
    h /=np.sum(h)
    perfectImage = nip.convolve(image, h)
    perfectImage *= NPhotons/np.max(perfectImage)
    gaussNoiseImage = nip.image(np.random.normal(perfectImage, stdv_gaussian))
    
    poissonNoiseImage = nip.noise.poisson(gaussNoiseImage, NPhot=100)
    
    return nip.image(poissonNoiseImage)
    