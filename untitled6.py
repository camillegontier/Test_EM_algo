#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct  1 16:56:40 2018

@author: camille
"""

import numpy as np
import math
import matplotlib.pyplot as plt
from scipy.stats import norm

#Number of points
N = 2

#First gaussian law
mu1 = 2
eta1 = 1
p1 = 1/3
x1 = np.random.normal(mu1,eta1,1)
#Second gaussian law
mu2 = 7
eta2 = 1
p2 = 2/3
x2 = np.random.normal(mu2,eta2,1)

#x = np.concatenate([x1,x2])
x = ([1.91494731, 7.26258436])

#Parameters initialization
mu1_est = 1
eta1_est = 2
#p1_est = 0.4
mu2_est = 3
eta2_est = 1
#p2_est = 0.6

for i in range(0,4):

    w_11 = norm.pdf(x[0], loc = mu1_est, scale = eta1_est)/(norm.pdf(x[0], loc = mu1_est, scale = eta1_est) + norm.pdf(x[0], loc = mu2_est, scale = eta2_est))
    #print(w_11)
    w_12 = norm.pdf(x[0], loc = mu2_est, scale = eta2_est)/(norm.pdf(x[0], loc = mu1_est, scale = eta1_est) + norm.pdf(x[0], loc = mu2_est, scale = eta2_est))
    #print(w_12)
    w_21 = norm.pdf(x[1], loc = mu1_est, scale = eta1_est)/(norm.pdf(x[1], loc = mu1_est, scale = eta1_est) + norm.pdf(x[1], loc = mu2_est, scale = eta2_est))

    w_22 = norm.pdf(x[1], loc = mu2_est, scale = eta2_est)/(norm.pdf(x[1], loc = mu1_est, scale = eta1_est) + norm.pdf(x[1], loc = mu2_est, scale = eta2_est))

    N1 = w_11 + w_21
    N2 = w_12 + w_22
    p1_est = N1/N 
    p2_est = N2/N 

    mu1_est = (1/N1)*(x[0]*w_11 + x[1]*w_21)
    mu2_est = (1/N2)*(x[0]*w_12 + x[1]*w_22)

    eta1_est = (1/N1)*(w_11*(x[0]-mu1_est)**2 + w_21*(x[1]-mu1_est)**2)
    eta2_est = (1/N2)*(w_12*(x[0]-mu2_est)**2 + w_22*(x[1]-mu2_est)**2)
    
print(mu1_est)
print(mu2_est)
print(eta1_est)
print(eta2_est)
print(p1_est)
print(p2_est)


#x = np.linspace(0,20, 100)
#y = norm.pdf(x, loc = 5, scale = 2)
#plt.plot(x,y)
