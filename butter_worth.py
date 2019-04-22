#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Mon Apr  1 13:54:23 2019

@author: rgukt
"""

import numpy as np
import matplotlib.pyplot as plt
gs=0.2
gp=0.8
wp=2*np.pi*4000
ws=2*np.pi*5000
def butter(gp,gs,wp,ws):
    a=(1/(gp**2))-1
    b=(1/(gs**2))-1
    N=int(np.ceil(0.5*np.log10(a/b)/np.log10(wp/ws)))
    wc=wp/(a**(1/(2*N)))
    return float(N),float(wc)
N,wc=butter(gp,gs,wp,ws)
print(N,wc)
w=np.arange(0,np.pi*2*10000,10)
b=np.abs(1/((1+(w/wc)**(2*N))**0.5))
plt.plot(w,b)
plt.show()