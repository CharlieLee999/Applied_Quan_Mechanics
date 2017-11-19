import numpy as np
import matplotlib.pyplot as plt
import scipy.special as special

mass = 1
hbar = 1
Angs2Atomic = 1.88973
um2Atomic = 18897.3
ev2Hartree = 27.2114
zero_1 = -2.338
zero_2 = -4.088
zero_3 = -5.521

### Parameters in eV and A unit
ev = 500
L = 12  

### Transfer parameters to atomic unit
eE = ev/ev2Hartree/um2Atomic
#eE = 1/ev2Hartree/Angs2Atomic
L = L * Angs2Atomic

### Argument z changes from -L/2 to very L/2 
start_point = -L/2
end_point = L/2
steps = 1000
E = eE * np.linspace(start_point, end_point * 10, steps)
#E = eE * np.linspace(-L/2, 50, steps)
z = E / eE

alpha = (2.0 * mass * eE/ hbar**2)**(1.0/3)

def get_epsilon(x, x_lf_rg):
    epsilon = alpha * (x_lf_rg - x)
    return epsilon
    
def normalize (psi_old, dx): 
    area = dx * np.trapz (psi_old ** 2)
    psi_new = psi_old / np.sqrt (area) 
    return psi_new

epsilon_left =  get_epsilon(z, start_point)  # alpha * (start_point - z)
epsilon_right = get_epsilon(z, end_point)    #alpha * (end_point - z)

airy_left = special.airy(epsilon_left)
airy_right = special.airy(epsilon_right)

D_func = airy_left[0] * airy_right[2] - airy_left[2] * airy_right[0]

wall_z = np.linspace(start_point, end_point, 100)
wall = eE * wall_z 


plt.figure()
plt.plot(E*ev2Hartree, D_func)
plt.ylim(-.5,1)
plt.xlabel('Energy/ eV')
plt.ylabel('$D (E)$')
plt.title('Energy - D(E)')
plt.grid()
plt.show()
plt.savefig('Energy-D(E)')

### Get the first three zeros of the D_func,

eigenenergy         = np.zeros(3)
eigen_cross_point   = np.zeros(3)
epsilon_left        = np.zeros(3)
epsilon_right       = np.zeros(3)

eigenenergy[0] = 0.24636 / ev2Hartree
eigenenergy[1] = 1.04883 / ev2Hartree
eigenenergy[2] = 2.35282 / ev2Hartree

eigen_cross_point = eigenenergy / eE
epsilon_left      = get_epsilon(eigen_cross_point, start_point)
epsilon_rigth     = get_epsilon(eigen_cross_point, end_point)

eigen_airy_func_left = special.airy(epsilon_left)
b_divided_a = -eigen_airy_func_left[0]/eigen_airy_func_left[2]

z_new = np.linspace(-L/2, L/2, steps)

epsilon_1 = alpha * (z_new - eigen_cross_point[0])
epsilon_2 = alpha * (z_new - eigen_cross_point[1])
epsilon_3 = alpha * (z_new - eigen_cross_point[2])

airy_func_1 = special.airy(epsilon_1)
airy_func_2 = special.airy(epsilon_2)
airy_func_3 = special.airy(epsilon_3)

wave_func_1 = airy_func_1[0] + b_divided_a[0] * airy_func_1[2]
wave_func_2 = airy_func_2[0] + b_divided_a[1] * airy_func_2[2]
wave_func_3 = airy_func_3[0] + b_divided_a[2] * airy_func_3[2]

dx = (end_point - start_point)/steps
wave_func_normed_1 = normalize(wave_func_1, dx)
wave_func_normed_2 = normalize(wave_func_2, dx)
wave_func_normed_3 = normalize(wave_func_3, dx)

plt.figure()
#plt.plot(z_new, wave_func_1**2 + eigenenergy[0], label = '$\phi^2 1$')
#plt.plot(z_new, wave_func_2**2 + eigenenergy[1], label = '$\phi^2 2$')
#plt.plot(z_new, wave_func_3**2 + eigenenergy[2], label = '$\phi^2 3$')

plt.plot(z_new, wave_func_normed_1**2 + eigenenergy[0], label = '$\phi^2 1$')
plt.plot(z_new, wave_func_normed_2**2 + eigenenergy[1], label = '$\phi^2 2$')
plt.plot(z_new, wave_func_normed_3**2 + eigenenergy[2], label = '$\phi^2 3$')


for i in range(0,3):
    plt.plot([-L/2, L/2], [eigenenergy[i], eigenenergy[i]],'k', linewidth = 0.8)


plt.plot([-L/2, -L/2],[wall[0], 1], 'k', linewidth = 1.2)
plt.plot([L/2, L/2], [wall[-1], 1], 'K', linewidth = 1.2)
plt.plot(wall_z, wall,'k', label = '$V(z)$', linewidth = 1.2)

plt.xlabel('Position z/ A')
plt.ylabel('$\phi^2 + E_i$')
plt.legend(loc = 'best')
plt.title('Modolous square of wavefunctions')

plt.ylim(wall[0], .2)
plt.show()

plt.savefig('Modolous_square_wavefunction_normed')

