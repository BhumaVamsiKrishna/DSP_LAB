#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sun Apr 21 10:34:11 2019

@author: rgukt
"""

import numpy as np
import matplotlib.pyplot as plt
n=np.arange(-10,20,.5)
f=input("enter small freq")
f=f*1.0
fs=input("enter large freq")
fs=fs*1.0
x=np.sin(2*np.pi*(f/fs)*n)
plt.stem(n,x)
plt.show()
p=input("enter current sample")
s=0
for i in range(p):
    s=s+x[i]
    
print("sum of all samples %f",s)
