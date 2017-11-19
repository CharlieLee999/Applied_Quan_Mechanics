# -*- coding: utf-8 -*-
"""
Created on Tue Nov 14 10:39:28 2017

@author: charlie
"""

import numpy as np
import scipy.special as special
import matplotlib.pyplot as plt

mass = 1.0
ev = 1.0
hbar = 1.0
Angs2Atomic = 1.88973
ev2Hatree = 27.2114
zero_1 = -2.338
zero_2 = -4.088
zero_3 = -5.521
eE = ev/ev2Hatree/Angs2Atomic

start_point = 0
end_point = 60
steps = 1000 * end_point
z = np.linspace(start_point,end_point, steps)

wall = eE * z

alpha = (2 * mass * eE/(hbar**2))**(1.0/3)

z_1 = -zero_1/ alpha
z_2 = -zero_2/ alpha
z_3 = -zero_3/ alpha

eigenenergy_1 = eE * z_1
eigenenergy_2 = eE * z_2
eigenenergy_3 = eE * z_3

### Print the crossing points of the wavefunction and the electric field
print('Crossing points are(atomic unit a):')
print z_1, z_2, z_3

### Print the eigenenergies in atomic unit
print('Eigenenergies are(atomic unit Hatree):')
print eigenenergy_1, eigenenergy_2, eigenenergy_3

### Plot the modolous square of wavefunction + eigenenergies 
epsilon_1 = alpha * (z - z_1)
epsilon_2 = alpha * (z - z_2)
epsilon_3 = alpha * (z - z_3)

phi_1 = special.airy(epsilon_1)
phi_2 = special.airy(epsilon_2)
phi_3 = special.airy(epsilon_3)

dx = alpha * (end_point - start_point)/(steps)

def normalize (psi_old, dx):
    area = dx * np.trapz (psi_old ** 2)
#    print area
    psi_new = psi_old / np.sqrt (area) 
    return psi_new
    
phi_1_normed = normalize(phi_1[0], dx)
phi_2_normed = normalize(phi_2[0], dx)
phi_3_normed = normalize(phi_3[0], dx)

fig = plt.figure()
#
#plt.plot(z, phi_1[0]**2 + eigenenergy_1, label = '$\phi^2 1$')
#plt.plot(z, phi_2[0]**2 + eigenenergy_2, label = '$\phi^2 2$')
#plt.plot(z, phi_3[0]**2 + eigenenergy_3, label = '$\phi^2 3$')

#plt.plot(z, phi_1_normed + eigenenergy_1, label = '$\phi 1$')
#plt.plot(z, phi_2_normed + eigenenergy_2, label = '$\phi 2$')
#plt.plot(z, phi_3_normed + eigenenergy_3, label = '$\phi 3$')

plt.plot(z, phi_1_normed**2 + eigenenergy_1, label = '$\phi^2 1$')
plt.plot(z, phi_2_normed**2 + eigenenergy_2, label = '$\phi^2 2$')
plt.plot(z, phi_3_normed**2 + eigenenergy_3, label = '$\phi^2 3$')

energy_line_1 = eigenenergy_1 * np.ones(steps)
energy_line_2 = eigenenergy_2 * np.ones(steps)
energy_line_3 = eigenenergy_3 * np.ones(steps)

plt.plot(z, energy_line_1, 'k', linewidth = 0.8)
plt.plot(z, energy_line_2, 'k', linewidth = 0.8)
plt.plot(z, energy_line_3, 'k', linewidth = 0.8)

plt.plot(z, wall,'k', label = 'Wall')

plt.xlim(0,60)
plt.ylim(0,1 )
plt.ylabel('$\Phi^2$')
plt.xlabel('$z / (a)$')
plt.title('Lowsest three eigenstates')
plt.legend(loc='best')
plt.grid()
plt.show()
fig.savefig('Square_wave_function_normed')
