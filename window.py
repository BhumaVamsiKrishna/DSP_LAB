#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Mon Apr  1 15:20:20 2019

@author: rgukt
"""
import numpy as np
import matplotlib.pyplot as plt
m=input("enter")
t1=np.arange(0,m/2,1)
x1=(2.0*t1/m)
t2=np.arange(m/2,m,1)
x2=3-((2.0*t2)/(m))
t=np.arange(0,m,1)
x3=0.5-0.5*np.cos(2*np.pi*t/m)
x4=0.54-0.46*np.cos(2*np.pi*t/m)
x5=0.42-(0.5*np.cos(2*np.pi*t/m))+(0.08*np.cos((4*np.pi*t)/(m)))
x6=1*t
plt.subplot(4,1,1)
plt.stem(t1,x1)
plt.stem(t2,x2)
plt.subplot(4,1,2)
plt.stem(x3)
plt.subplot(4,1,3)
plt.stem(x4)
plt.subplot(4,1,4)
plt.stem(x5)
plt.subplot(4,1,5)
plt.stem(x6)
plt.show()
