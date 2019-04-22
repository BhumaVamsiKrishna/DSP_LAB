#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sun Mar 24 18:25:20 2019

@author: mahesh
"""

import numpy as np
import matplotlib.pyplot as plt
y=[]
x=input("enter")
h=input("enter")
l1=len(x)
l2=len(h)
for n in range(0,l1+l2-1,1):
    s=0
    for k in range(0,l1,1):
        if(n-k>=0 and n-k<l1):
         s=s+x[k]*h[n-k]
    y.append(s)
print y
t=np.linspace(0,l1+l2-2,l1+l2-1)
plt.stem(t,y)
plt.show()