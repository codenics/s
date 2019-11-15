#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov 14 21:26:33 2019

@author: codenics
"""

import numpy as np
import pandas as pd


#Does not include 1st line treat it as header
pdpic = pd.read_csv("picture.txt")
#Convert into numpy array of strings, each line is a string
npdata = pdpic.to_numpy()
#Takes away the last element[-1]
npdata = npdata[:199,:]

#We use the dimenstions in the file, just to save time
pic_data = np.ones((199, 179))

#Creates an emptyList:::Use arrayList in Java
countColor = []*0
eachRow = []*0
for i, each_line in enumerate(npdata):
    for j, valueEachLine in enumerate(each_line):
        onerow = countColor.append(each_line[j])
    eachRow.append(onerow)
        
        
    