# -*- coding: utf-8 -*-
"""
Created on Thu Dec  7 15:57:17 2017

@author: charlie
"""

import numpy as np
import matplotlib.pyplot as plt

N = input("Please input the max number of Legendre polynomials:")
Legen_poly = [0] * N
Legen_poly_deri = [0] * N

Legen_poly_ii1   = [0] * N
Legen_poly_ii1_left   = [0] * N
Legen_poly_ii1_right   = [0] * N

Legen_poly_ii2  = [0] * N
Legen_poly_ii2_left   = [0] * N
Legen_poly_ii2_right   = [0] * N

Legen_poly_multp = [0] * N**2
Legen_poly_inter = np.zeros(N**2)

### Initialization P_n
Legen_poly[0] = np.poly1d([1])
Legen_poly[1] = np.poly1d([1, 0])

### Calculate P[n+1] with P[n] and P[n-1]
for n in range(1, N-1):
    Legen_poly[n+1] = ((2*n+1) * np.poly1d([1, 0]) * Legen_poly[n] - \
                        n * Legen_poly[n-1])/(n+1)

### Print the Legendre polynomial 
for n in range(0, N):
    print 'P['+ str(n) + ' ] is '    
    print Legen_poly[n]
    print('\n')

### Indefinite integration of  P_n * P_m
for i in range(0, N):
    for j in range(0, N):
        Legen_poly_multp[i*N+j] = np.polyint(Legen_poly[i] * Legen_poly[j])

### Calculate the definite circulus from -1 to +1
for n in range(0, N**2):
    Legen_poly_inter[n] = Legen_poly_multp[n](1) - Legen_poly_multp[n](-1)

Legen_poly_inter = Legen_poly_inter.reshape((N, N))

### 1.ii 
for n in range(0, N):
#    Legen_poly_deri[n] = np.polyder(Legen_poly[n])
#    print Legen_poly_deri[n]
    Legen_poly_ii1_left[n] = -np.polyder( np.poly1d([-1, 0, 1]) * np.polyder(Legen_poly[n]) )
    Legen_poly_ii1_right[n] = n * (n+1) * Legen_poly[n]    
    Legen_poly_ii1[n] =  Legen_poly_ii1_left[n] - Legen_poly_ii1_right[n]
    
    print ('The left and right parts of problem 1.ii are ')
    print Legen_poly_ii1_left[n]
    print Legen_poly_ii1_right[n]
    print ('The differene of left and right part of problem 1.ii is ' + str(Legen_poly_ii1[n]))
#    print Legen_poly_ii1[n]
    print ('\n')

### 1.iii 

for n in range(0, N):
    Legen_poly_ii2_left[n] = np.poly1d([-1, 0, 1]) * np.polyder(Legen_poly[n])
    Legen_poly_ii2_right[n] = n *( Legen_poly[n-1] - np.poly1d([1, 0]) * Legen_poly[n] ) 
    Legen_poly_ii2[n] =  Legen_poly_ii2_left[n] - Legen_poly_ii2_right[n]
    print ('The left and right parts of problem 1.iii are ')
    print Legen_poly_ii2_left[n]
    print Legen_poly_ii2_right[n]
    print ('The differene of left and right part of problem 1.iii is ' + str(Legen_poly_ii2[n]))
#    print Legen_poly_ii2[n]
    print ('\n')
