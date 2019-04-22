#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sun Apr 14 09:39:03 2019

@author: mahesh
"""

import numpy as np
import matplotlib.pyplot as plt
rxx=[]
x=input("enter")
l1=len(x)
for l in range(-(l1-1),l1,1):
    s=0
    for n in range(0,l1,1):
        if(n+l>=0 and n+l<l1):
         s=s+x[n]*x[n+l]
    rxx.append(s)
print rxx
t=np.linspace(-(l1-1),l1-1,2*l1-1)
plt.stem(t,rxx)
plt.show()
