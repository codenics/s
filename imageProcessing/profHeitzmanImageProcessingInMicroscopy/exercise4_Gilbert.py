#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec  4 15:53:18 2019

@author: codenics
"""
#%%
import NanoImagingPack as nip
import matplotlib.pyplot as plt
import numpy as np

#Variables used by subsequent implementations
pupil = nip.rr(obj.shape) < 50
h = nip.abssqr(nip.ift2d(pupil))
otf = nip.ft(h)*np.sqrt(np.prod(h.shape))
h/=np.sum(h)
Niter = 200
    
    
#%% ================================Task1======================================

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
    
# %% ================================Task2=====================================
# Richardson Lucy implementation
def richardSonLucy(image):    
    #Creates a noicy image from SimMicroscope method in Task 1
    noiseImage = image
    estimate = noiseImage*0.0+np.mean(noiseImage)
    for n in range(1, Niter):
        fn = np.real(nip.ift(nip.ft(estimate)*otf))
        estimate *=np.real( nip.ift(nip.ft(noiseImage/fn)*np.conj(otf)))
        estimate /=np.max(estimate)*100
    return estimate

# %% ================================Task3=====================================
    # Richardson Lucy with Gaussian Prior
def richardSonLucyGaussianPrior(image):
    noiseImage = nip.readim(image)
    obj = nip.readim('lena.png')
    lamda = 0.01#TV
    estimate = noiseImage*0.0+np.mean(noiseImage)
    for n in range(1, Niter):
        fn = np.real(nip.ift(nip.ft(estimate)*otf))
        estimate *=np.real(nip.ift(nip.ft(noiseImage/fn)*np.conj(otf)) + (lamda*np.square(obj) + 2*lamda*obj))
        estimate /=np.max(estimate)*100
    return estimate

#%% ================================Task3======================================
figure, axes = plt.subplots(2,3)
axes[0, 0] = plt.imshow(richardSonLucy(SimMicroscope('lena.png', radius=50, stdv_gaussian = 5)))
axes[0, 1] = plt.imshow(richardSonLucy(SimMicroscope('lena.png', radius=75, stdv_gaussian = 5)))
axes[0, 2] = plt.imshow(richardSonLucy(SimMicroscope('lena.png', radius=100, stdv_gaussian = 5)))
axes[1, 0] = plt.imshow(richardSonLucy(SimMicroscope('lena.png', radius=50, stdv_gaussian = )))
axes[1, 1] = plt.imshow(richardSonLucy(SimMicroscope('lena.png', radius=50, stdv_gaussian = 5)))
axes[1, 1] = plt.imshow(richardSonLucy(SimMicroscope('lena.png', radius=50, stdv_gaussian = 5)))
axes[1, 0] = plt.imshow(richardSonLucy(SimMicroscope('lena.png', radius=50, stdv_gaussian = 5)))