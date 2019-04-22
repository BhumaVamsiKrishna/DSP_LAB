#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sun Apr 14 07:21:08 2019

@author: mahesh
"""

import numpy as np
import matplotlib.pyplot as plt
rxy=[]
x=np.array(input('enter seq 1='))
y=np.array(input('enter seq 2='))
l1=len(x)
l2=len(y)
for l in range(-7,7,1):
    s=0
    for n in range(0,l1,1):
        if(n+l>=0 and n+l<l1):
         s=s+x[n]*y[n+l]
    rxy=np.append(rxy,s)
print ("rxy=", rxy)

n=np.linspace(-7,6,14)
plt.figure(1)
plt.xlabel("time")
plt.ylabel("amplitude")
plt.title("cross  correlation")
plt.stem(n,rxy)