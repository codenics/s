#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov 22 14:36:11 2019

@author: codenics
nip.extract()
OTF = autocorrelation(CTF)
= iFT((FT(CT).FT(CT)*))
Fix point convolution
"""

import numpy as np
import NanoImagingPack as nip
import matplotlib.pyplot as plt

#%%


myobject = nip.readim()
mysize = myobject.shape

#coherent PSF filtering
myNA = 0.25
mypupil = nip.rr(mysize, freq='ftfreq')<myNA

#simulate a coherent imaging scenario
mybfp = nip.ft(myobject)*mypupil
myobject = nip.ift(mybfp)

# incoherent OTF filtering
myotf = nip.ifft(nip.ft(mypupil)*np.conj(nip.ft(mypupil)))

# compare the transmission function of CTF and OTF
plt.figure()
plt.subplot(121)
plt.title('CTF')
plt.plot(mypupil[:, mysize[0]//2])

plt.subplot(122)
plt.title('OTF')
plt.plot(myotf[:, mysize[0]//2])

#%%
# Compute the 3D coherent transfer function
#but first only in x/z

my_radius_outer = 100
my_radius_inner = 99
mycircle = (nip.rr(mysize))<my_radius_outer*(nip.rr(mysize))>my_radius_inner
myctf_xz = mycircle*(np.abs(nip.phiphi(mysize))<0.5)

myobj = 

#convolve scatterer with CTF in 3D (X/Z)
myimage = np.abs(nip.ift(myctf_xz*nip.ft(myobject)))