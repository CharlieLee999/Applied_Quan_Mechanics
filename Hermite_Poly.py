# -*- coding: utf-8 -*-
"""
Created on Tue Nov 21 21:20:15 2017

@author: charlie
"""

if __name__ == "__main__":
    pass
from sympy import symbols, zeros, simplify
import numpy as np
import matplotlib.pyplot as plt
x = symbols('x')
n = input('Please input the number of term of polymonials (n>2):')

a = np.zeros(n)

def Get_Hermite_poly(x, n):
    H = zeros(1, n)
    H[0] = 1
    H[1] = 2 * x
    for i in range(1, n-1):
        H[i+1] = 2 * x * H[i] - 2 * i * H[i-1]
    return H

def Get_plotable_hermite(Hermite_poly_i,xx):
    plot_herm = Hermite_poly_i.subs(x, xx)   
    return plot_herm

Hermite_poly = Get_Hermite_poly(x, n)
Hermite_poly = simplify(Hermite_poly)

for i in range(0, n):
    print "H[", i, "]= ", Hermite_poly[i]

#print type(Hermite_poly)
#coeff = Hermite_poly[2].coeffs()
#print coeff

plt.figure()
steps = 100
xx = np.linspace(-3, 3, steps)
plot_herm_i = np.zeros(steps)
for i in range(0, n):
    for j in range(0, steps):
        plot_herm_i[j] = Get_plotable_hermite(Hermite_poly[i], xx[j])
    type(plot_herm_i[1])
    if i>0:
        plt.plot(xx, plot_herm_i/(1.0*i*i),label='H['+str(i)+']'+'/'+str(i)+'^2')
    else:
        plt.plot(xx, plot_herm_i,label='H['+str(i)+']')

#plt.grid()
#plt.legend(loc = 'best')
#plt.ylim((-10,10))
#plt.xlabel('$x$')
#plt.ylabel('$H_i (x)$')
#plt.title('Hermite Polynomials')
#plt.savefig('Hermite_poly')
#plt.show()
