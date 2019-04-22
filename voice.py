#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sun Apr 21 08:50:00 2019

@author: rgukt
"""

import scipy.io.wavfile as wav
import numpy as np
from matplotlib import pyplot as plt
fs,data=wav.read('akon.wav')
print(fs,len(data),data)
plt.subplot(121)
plt.plot(data)
t=np.arange(0,(len(data)*1.0)/fs,1.0/fs)
plt.subplot(122)
plt.plot(t,data)
plt.show()
wav.write('akon-fast.wav',2*fs,data)
wav.write('akon-slow.wav',1*fs,data)
