# -*- coding: utf-8 -*-
"""
Created on Fri Sep 28 08:53:50 2018

@author: camille
"""

import numpy as np
import math
import matplotlib.pyplot as plt
from scipy.stats import norm

#Number of points
N = 10
#First gaussian law
mu1 = 3
eta1 = 5
p1 = 0.3
x1 = np.random.normal(mu1,eta1,int(p1*N))
#Second gaussian law
mu2 = 7
eta2 = 1
p2 = 0.7
x2 = np.random.normal(mu2,eta2,int(p2*N))

x = np.concatenate([x1,x2])

#Parameters initialization
mu1_est = 1
eta1_est = 2
p1_est = 0.4
mu2_est = 3
eta2_est = 1
p2_est = 0.6

for i in range(0,100):
    #E step : computation of p1 and p2 (weights computation)
    w_11 = norm.pdf(x[0], loc = mu1_est, scale = eta1_est)*p1_est \
        /(norm.pdf(x[0], loc = mu1_est, scale = eta1_est)*p1_est + \
          norm.pdf(x[0], loc = mu2_est, scale = eta2_est)*p2_est)
    w_21 = norm.pdf(x[1], loc = mu1_est, scale = eta1_est)*p1_est \
        /(norm.pdf(x[1], loc = mu1_est, scale = eta1_est)*p1_est + \
          norm.pdf(x[1], loc = mu2_est, scale = eta2_est)*p2_est)
    w_31 = norm.pdf(x[2], loc = mu1_est, scale = eta1_est)*p1_est \
        /(norm.pdf(x[2], loc = mu1_est, scale = eta1_est)*p1_est + \
          norm.pdf(x[2], loc = mu2_est, scale = eta2_est)*p2_est)
    w_41 = norm.pdf(x[3], loc = mu1_est, scale = eta1_est)*p1_est \
        /(norm.pdf(x[3], loc = mu1_est, scale = eta1_est)*p1_est + \
          norm.pdf(x[3], loc = mu2_est, scale = eta2_est)*p2_est)
    w_51 = norm.pdf(x[4], loc = mu1_est, scale = eta1_est)*p1_est \
        /(norm.pdf(x[4], loc = mu1_est, scale = eta1_est)*p1_est + \
          norm.pdf(x[4], loc = mu2_est, scale = eta2_est)*p2_est)
    w_61 = norm.pdf(x[5], loc = mu1_est, scale = eta1_est)*p1_est \
        /(norm.pdf(x[5], loc = mu1_est, scale = eta1_est)*p1_est + \
          norm.pdf(x[5], loc = mu2_est, scale = eta2_est)*p2_est)
    w_71 = norm.pdf(x[6], loc = mu1_est, scale = eta1_est)*p1_est \
        /(norm.pdf(x[6], loc = mu1_est, scale = eta1_est)*p1_est + \
          norm.pdf(x[6], loc = mu2_est, scale = eta2_est)*p2_est)
    w_81 = norm.pdf(x[7], loc = mu1_est, scale = eta1_est)*p1_est \
        /(norm.pdf(x[7], loc = mu1_est, scale = eta1_est)*p1_est + \
          norm.pdf(x[7], loc = mu2_est, scale = eta2_est)*p2_est)
    w_91 = norm.pdf(x[8], loc = mu1_est, scale = eta1_est)*p1_est \
        /(norm.pdf(x[8], loc = mu1_est, scale = eta1_est)*p1_est + \
          norm.pdf(x[8], loc = mu2_est, scale = eta2_est)*p2_est)
    w_101 = norm.pdf(x[9], loc = mu1_est, scale = eta1_est)*p1_est \
        /(norm.pdf(x[9], loc = mu1_est, scale = eta1_est)*p1_est + \
          norm.pdf(x[9], loc = mu2_est, scale = eta2_est)*p2_est)
        
    w_12 = norm.pdf(x[0], loc = mu2_est, scale = eta2_est)*p2_est \
        /(norm.pdf(x[0], loc = mu1_est, scale = eta1_est)*p1_est + \
          norm.pdf(x[0], loc = mu2_est, scale = eta2_est)*p2_est)
    w_22 = norm.pdf(x[1], loc = mu2_est, scale = eta2_est)*p2_est \
        /(norm.pdf(x[1], loc = mu1_est, scale = eta1_est)*p1_est + \
          norm.pdf(x[1], loc = mu2_est, scale = eta2_est)*p2_est)
    w_32 = norm.pdf(x[2], loc = mu2_est, scale = eta2_est)*p2_est \
        /(norm.pdf(x[2], loc = mu1_est, scale = eta1_est)*p1_est + \
          norm.pdf(x[2], loc = mu2_est, scale = eta2_est)*p2_est)
    w_42 = norm.pdf(x[3], loc = mu2_est, scale = eta2_est)*p2_est \
        /(norm.pdf(x[3], loc = mu1_est, scale = eta1_est)*p1_est + \
          norm.pdf(x[3], loc = mu2_est, scale = eta2_est)*p2_est)
    w_52 = norm.pdf(x[4],loc = mu2_est, scale = eta2_est)*p2_est \
        /(norm.pdf(x[4], loc = mu1_est, scale = eta1_est)*p1_est + \
          norm.pdf(x[4], loc = mu2_est, scale = eta2_est)*p2_est)
    w_62 = norm.pdf(x[5], loc = mu2_est, scale = eta2_est)*p2_est \
        /(norm.pdf(x[5], loc = mu1_est, scale = eta1_est)*p1_est + \
          norm.pdf(x[5], loc = mu2_est, scale = eta2_est)*p2_est)
    w_72 = norm.pdf(x[6], loc = mu2_est, scale = eta2_est)*p2_est \
        /(norm.pdf(x[6], loc = mu1_est, scale = eta1_est)*p1_est + \
          norm.pdf(x[6], loc = mu2_est, scale = eta2_est)*p2_est)
    w_82 = norm.pdf(x[7], loc = mu2_est, scale = eta2_est)*p2_est \
        /(norm.pdf(x[7], loc = mu1_est, scale = eta1_est)*p1_est + \
          norm.pdf(x[7], loc = mu2_est, scale = eta2_est)*p2_est)
    w_92 = norm.pdf(x[8], loc = mu2_est, scale = eta2_est)*p2_est \
        /(norm.pdf(x[8], loc = mu1_est, scale = eta1_est)*p1_est + \
          norm.pdf(x[8], loc = mu2_est, scale = eta2_est)*p2_est)
    w_102 = norm.pdf(x[9], loc = mu2_est, scale = eta2_est)*p2_est \
        /(norm.pdf(x[9], loc = mu1_est, scale = eta1_est)*p1_est + \
          norm.pdf(x[9], loc = mu2_est, scale = eta2_est)*p2_est)   
    
    #M step : maximization of Q
    N1 = w_11 + w_21 +w_31 + w_41 + w_51 + w_61 + w_71 + w_81 + w_91 + w_101
    N2 = w_12 + w_22 +w_32 + w_42 + w_52 + w_62 + w_72 + w_82 + w_92 + w_102
    p1_est = N1/N
    p2_est = N2/N
    mu1_est = (1/N1)*(w_11*x[0] + w_21*x[1] + w_31*x[2] + w_41*x[3] + w_51*x[4] + \
              w_61*x[5] + w_71*x[6] + w_81*x[7] + w_91*x[8] + w_101*x[9])
    mu2_est = (1/N2)*(w_12*x[0] + w_22*x[1] + w_32*x[2] + w_42*x[3] + w_52*x[4] + \
              w_62*x[5] + w_72*x[6] + w_82*x[7] + w_92*x[8] + w_102*x[9])
    
    eta1_est = (1/N1)*(w_11*(x[0]-mu1_est)**2 + w_21*(x[1]-mu1_est)**2 + w_31*(x[2]-mu1_est)**2 + w_41*(x[3]-mu1_est)**2 + w_51*(x[4]-mu1_est)**2 + \
              w_61*(x[5]-mu1_est)**2 + w_71*(x[6]-mu1_est)**2 + w_81*(x[7]-mu1_est)**2 + w_91*(x[8]-mu1_est)**2 + w_101*(x[9]-mu1_est)**2)
    eta2_est = (1/N2)*(w_12*(x[0]-mu2_est)**2 + w_22*(x[1]-mu2_est)**2 + w_32*(x[2]-mu2_est)**2 + w_42*(x[3]-mu2_est)**2 + w_52*(x[4]-mu2_est)**2 + \
              w_62*(x[5]-mu2_est)**2 + w_72*(x[6]-mu2_est)**2 + w_82*(x[7]-mu2_est)**2 + w_92*(x[8]-mu2_est)**2 + w_102*(x[9]-mu2_est)**2)
    
print(mu1_est)
print(mu2_est)


