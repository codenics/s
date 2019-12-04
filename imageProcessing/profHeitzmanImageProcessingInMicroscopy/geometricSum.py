#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Nov 30 19:16:34 2019

@author: codenics
"""

from sympy import  sieve

def mathSum(n):
    summed = (8*((8**n) - 1))/7
    return summed
    

#or i in range(1, 21):
   #print(i, "  " ,mathSum(i))
    
   
   

def isPrimenk(n, k):
    canga =  int((3**(4*n)) + (4*(7**(4*k))))
    return canga

for i in range(16):
    for j in range(16):
        print(isPrimenk(i,j) in sieve, "\t", isPrimenk(i,j), "\t", i , "\t", j)