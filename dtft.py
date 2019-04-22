#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sun Mar 24 17:18:09 2019

@author: mahesh
"""

import numpy as np
import matplotlib.pyplot as plt
import cmath as mp
x=input('enter a seq')
y=[]
j=mp.sqrt(-1)
w=np.linspace(-2*np.pi,2*np.pi,10000)
for W in range(0,len(w),1):
    s=0
    for n in range(0,len(x),1):
        s=s+x[n]*np.exp(-j*w[W]*n)
    y=np.append(y,s)
w=np.linspace(-np.pi,np.pi,10000)
plt.figure(1)
plt.title("Magnitude plot")
plt.xlabel("frequency")
plt.ylabel("amplitude")
plt.plot(w,np.abs(y))
plt.figure(2)
plt.title("Phase plot")
plt.xlabel("frequency")
plt.ylabel("angle")
plt.plot(w,np.angle(y))


