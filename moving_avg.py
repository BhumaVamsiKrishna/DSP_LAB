#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sun Apr 21 11:15:03 2019

@author: rgukt
"""

import numpy as np
import matplotlib.pyplot as plt
f=input("enter freq")
t=np.linspace(0,100,1000)
x=np.sin(2*np.pi*f*t)
n=np.random.rand(x.shape[0])
c=x+n
y=[]
p=input("enter order")
for i in range(1000):
    m=0
    d=p
    if(i<p):
        d=i
    for j in range(d+1):
        m=m+c[i-j]
    y.append(m/p)
plt.subplot(4,1,1)
plt.plot(t,x)
plt.subplot(4,1,2)
plt.plot(t,n)
plt.subplot(4,1,3)
plt.plot(t,c)
plt.subplot(4,1,4)
plt.plot(t,y)
plt.show()






