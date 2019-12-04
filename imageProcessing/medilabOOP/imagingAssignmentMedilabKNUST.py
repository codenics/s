
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov 14 21:26:33 2019

@author: codenics
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

#Does not include 1st line treat it as header
pdpic = pd.read_csv("picture.txt")
#Convert into numpy array of strings, each line is a string
npdata = pdpic.to_numpy()


#Takes away the last element[-1]
npdata = npdata[:199]

#Create two empty lists
all_lines = []*0
pic_values = np.ones((199, 174))
#Loop through all lines and split 
#them as string(Each line is represented as a string)
for i, oneine in enumerate(npdata):
    all_lines.append(npdata[i,0].split())
    
    
#Loop again in the inner loop changing the 'character' to an integer
for i in all_lines:
    for j, k in enumerate(i):
        i[j] = int(i[j])
        
#Now convert to an integer array:: Same shape as original
np_picture = np.array(all_lines)

#Cool algorithm to write the pixel value. 'Don't ask me! :) '
for i in range(len(all_lines)):
    for j in range(1, len(all_lines[i])):
        if j-1<all_lines[i][j-1]:
            pic_values[i][j-1:all_lines[i][j-1]] = int(all_lines[i][j])
        else:
            continue 

print(pic_values) 
plt.imshow(pic_values)
