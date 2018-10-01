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
N = 3

#First gaussian law
mu1 = 2
eta1 = 1
p1 = 1/3
x1 = np.random.normal(mu1,eta1,1)
#Second gaussian law
mu2 = 7
eta2 = 1
p2 = 2/3
x2 = np.random.normal(mu2,eta2,2)

x = np.concatenate([x1,x2])
print(x)