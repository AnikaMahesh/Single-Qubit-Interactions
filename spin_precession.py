# Save as spin_precession.py or run in a notebook
import numpy as np
import matplotlib.pyplot as plt
from qutip import basis, sigmax, sigmay, sigmaz, mesolve, expect, Bloch, Qobj


g = 2.0           
mu_B = 1.0              
Omega = 1.0            
B = np.array([0.0, 0.0, 1.0]) 
n = B / np.linalg.norm(B)


H = -(Omega/2.0) * (n[0]*sigmax() + n[1]*sigmay() + n[2]*sigmaz())

psi0 = (basis(2,0) + basis(2,1)).unit()
tlist = np.linspace(0, 10, 400)

result = mesolve(H, psi0, tlist, [], [sigmax(), sigmay(), sigmaz()])

sx = np.real(result.expect[0])
sy = np.real(result.expect[1])
sz = np.real(result.expect[2])
plt.figure(figsize=(8,4))
plt.plot(tlist, sx, label=r'$\langle\sigma_x\rangle$')
plt.plot(tlist, sy, label=r'$\langle\sigma_y\rangle$')
plt.plot(tlist, sz, label=r'$\langle\sigma_z\rangle$')
plt.xlabel('time (arb. units)')
plt.ylabel('Expectation value')
plt.legend()
plt.title('Spin precession in B along z (initial |+x>)')
plt.grid(True)
plt.show()


b = Bloch()
b.add_points([sx, sy, sz])

b.point_marker = ['o']
b.marker_size = [3]
b.show()