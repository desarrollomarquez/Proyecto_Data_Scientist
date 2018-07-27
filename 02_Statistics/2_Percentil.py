# -*- coding: utf-8 -*-
"""
Created on Fri Jul 27 10:36:03 2018

@author: diego
"""
import numpy as np
import matplotlib.pyplot as plt
from statistics import mode
from scipy import stats
import statsmodels.api as sm
import pylab

dist = []
N = 47
dist= np.random.randint(low = 51, high = 99, size = N)
dist_order = np.sort(dist)
print(dist_order)
#%% 1. Percentile Ecuation
x = 12 #  Interest Number  Sequence Position -> 63 score
percentil = ((x - 0.5)/N)*100
print("Percentile :P\n{}\n ".format(percentil),"is 63 Score")
#%% 2. Percentile Ecuation
print("1st quartile: ",np.percentile(percentil, 25))
print("2st quartile: ",np.percentile(percentil, 50))
print("3st quartile: ",np.percentile(percentil, 75))
#%% Graph Quantiles 
sm.qqplot(dist_order, line='45')
pylab.show()