#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov 29 14:49:47 2019

@author: codenics
"""

import NanoImagingPack as nip
import numpy as np

obj = nip.readim()
#pupil = nip.rr() < 50

pupil = nip.rr(obj.shape) < 50

h = nip.abssqr(nip.ift2d(pupil))

h/=np.sum(h)

perfectImage = nip.convolve(obj, h)
NPhoton = 100

perfectImage *= NPhoton / np.max(perfectImage)


noiseImage = nip.noise.poisson(perfectImage)

#Generalized Wiener filtering
otf = nip.ft(h)*np.sqrt(np.prod(h.shape))
myconst = 0.000001
#otf/=np.max(np.abs(otf))

fimg = np.real(nip.ift(nip.ft(noiseImage)* np.conj(otf)/(nip.abssqr(otf) + myconst)))

nip.catE



#Richardson Lucy implementation

Niter = 100
estimate = noiseImage*0.0+np.mean(noiseImage)
for n in range(1, 100):
    fwd = np.real(nip.ift(nip.ft(estimate)*otf))
    
    estimate *=np.real( nip.ift(nip.ft(noiseImage/fwd)*np.conj(otf)))

nip.cat((obj, fimg, estimate, obj), -3)

"""

Richardson Lucy implementation

Niter = 100
estimate = noiseImage*0.0+np.mean(noiseImage)
for n in range(1, 100):
    fwd = np.real(nip.ift(nip.ft(estimate)*otf))
    estimate *= np.real(nip.ift(nip.ft(noiseImage/fwd)*np.conj(otf)) + )

nip.cat((obj, fimg, estimate, obj), -3)
"""