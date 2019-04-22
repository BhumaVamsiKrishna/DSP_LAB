#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 18 22:04:55 2019

@author: mahesh
"""

import numpy as np
import matplotlib.pyplot as plt
import cmath as mp

x=np.array(input('enter seq='))
N=input('enter N_point dft value')
y=[]
j=mp.sqrt(-1)
for k in range(0,N,1):
    s=0
    for n in range(0,len(x),1):
        p=np.exp((-j*n*k*2*np.pi)/N)
        s=s+x[n]*p
    y=np.append(y,s)
print np.abs(y)
w=np.linspace(0,N-1,N)
plt.figure(1)
plt.xlabel("time")
plt.ylabel("amplitude")
plt.title("Magnitude plot")
#plt.subplot(2,1,1)
plt.stem(w,(np.abs(y))) 
plt.figure(2)
#plt.subplot(2,1,2)
plt.xlabel("time")
plt.ylabel("angle")
plt.title("Angle plot")
plt.stem(w,np.angle(y))  