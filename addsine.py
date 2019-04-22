#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sun Apr 21 08:34:57 2019

@author: rgukt
"""

import numpy as np
import matplotlib.pyplot as plt
time=np.arange(0,100,0.01)
a=0
a1=100
f=100
f1=500
s1=np.sin(6.28*f*time+a)
s2=np.sin(6.28*f1*time+a1)
s3=s1+s2
plt.subplot(2,2,1)
plt.plot(time,s1)
plt.subplot(2,2,2)
plt.plot(time,s2)
plt.subplot(2,2,3)
plt.plot(time,s3)
plt.xlabel("time")
plt.ylabel("s3")
plt.show()