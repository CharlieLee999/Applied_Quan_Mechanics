import numpy as np
import scipy.special as special 
import matplotlib.pyplot as plt

mass = 1.0
hbar = 1.0
Angs2Atomic = 1.88973
ev2Hartree = 27.2114
#Angstorm = 1.0e-10
ev = 1.0
#eE = ev/Angstorm
eE = ev/ev2Hartree/Angs2Atomic

### Input the lowest energy E  and turning point
E = eE * 5
#turn_point = 6.90057

### Iteration steps
start_point_right =  5 + 30.0 * Angs2Atomic # turn_point 

steps = int(start_point_right * 100)

### Initialize the position and function value
z = np.linspace(0, start_point_right, steps + 1)
U = np.zeros(z.size)

### Starting position and function value phi_1, phi_2 
#airy_0 = special.airy(start_point_right)
#airy_1 = special.airy(z[-2])

airy_0 = special.airy(z[0])
airy_1 = special.airy(z[1])

U[0] = airy_0[0]
U[1] = airy_1[0]

def get_k_square(x):
    return 2 * mass * (E - eE * x) / hbar**2

def get_U_i_minus_1(U_0, U_plus, k_square_minus, k_square_0, k_square_plus):
    term_0 = 2.0 * (1 - 5.0 * hbar**2 * k_square_0/12) * U_0
    term_1 = (1 + 1.0 * hbar**2 * k_square_plus/12) * U_plus
    term_minus_1 = (1 + 1.0 * hbar**2 * k_square_minus/12)
#    print term_0, term_1
    return (term_0 - term_1)/term_minus_1
    
def get_U_i_plus_1(U_0, U_minus, k_square_minus, k_square_0, k_square_plus):
    term_0 = 2.0 * (1 - 5.0 * hbar**2 * k_square_0/12) * U_0
    term_plus_1 = (1 + 1.0 * hbar**2 * k_square_plus/12) 
    term_minus_1 = (1 + 1.0 * hbar**2 * k_square_minus/12) * U_minus
    return (term_0 - term_minus_1)/term_plus_1
    
#i = int(steps) - 1
#while i > 0:
#    k_sqr_p  = get_k_square(z[i+1])
#    k_sqr_0  = get_k_square(z[i])
#    k_sqr_m  = get_k_square(z[i-1])
#    U[i-1]   = get_U_i_minus_1(U[i], U[i+1], k_sqr_m, k_sqr_0, k_sqr_p)
#    i -= 1

i = 1
while i < steps-1:
    k_sqr_p  = get_k_square(z[i+1])
    k_sqr_0  = get_k_square(z[i])
    k_sqr_m  = get_k_square(z[i-1])
    U[i+1]   = get_U_i_plus_1(U[i], U[i-1], k_sqr_m, k_sqr_0, k_sqr_p)
    i += 1
    
plt.figure()
plt.plot(z,U)
plt.show()
