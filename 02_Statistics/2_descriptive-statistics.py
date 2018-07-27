# -*- coding: utf-8 -*-
"""
Created on Fri Jul 27 09:32:22 2018

@author: diego
"""

import numpy as np
from statistics import mode
import matplotlib.pyplot as plt
from scipy import stats
import scipy.stats as sp

# Create a dataset
distribution=[1,1,1,4,6,8,3,25,7,56,45,67,89,44,44,6,56,34,23,43,46,8,99,9,9,9,9,0,3,4,4,4,4,4,5,12,13,14,15]
dist=np.array(distribution)
print("Our Distribution: ",dist)
# Apply functions
#%%
print("Number of scores: ",len(dist))
print("Number of uniques scores: ",len(np.unique(dist)))
print("Sum: ",sum(dist))
print("Maximum: ",max(dist))
print("Minimum: ",min(dist))
print("Range: ",max(dist)-min(dist))
print("Mean: ",np.mean(dist, axis=0))
print("Median: ",np.median(dist, axis=0))
print("Mode: ",stats.mode(dist)[0][0]) #yes, numpy doesn't support mode functionality
print("Variance: ",np.var(dist, axis=0))
print("Standard Deviation: ",np.std(dist, axis=0))
print("1st quartile: ",np.percentile(dist, 25))
print("3rd quartile: ",np.percentile(dist, 75))
print("Interquartile Range: ",np.percentile(dist, 75)-np.percentile(dist, 25))
print("Distribution Skew: ",stats.skew(dist))
print("Distribution Kurtosis: ",stats.kurtosis(dist))
print("Order Unique:",np.unique(np.sort(dist)))
print("order Median:",np.median(np.unique(np.sort(dist))))
# Print results
#print('Mean: {}, median: {}'.format(dataset_mean, dataset_median)
#%%
plt.hist(dist, bins=len(dist))
plt.yticks(np.arange(0, 15, 1.0))
plt.title('Histogram of distribution scores')
plt.show()
