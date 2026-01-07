import numpy as np
import matplotlib.pyplot as plt
from qutip import *

# Parameters
hbar = 1.0        # we can set ħ = 1 in natural units
Omega = 1.0       # Rabi frequency



plt.figure()
for Delta in [0, 0.2, 0.4, 0.6, 0.8, 1.0]:   # detuning

    # Hamiltonian: (h/2)(Ω σx - Δ σz)
    H = 0.5 * (Omega * sigmax() - Delta * sigmaz())

    # Initial state |0>
    psi0 = basis(2, 0)

    # Time points
    tlist = np.linspace(0, 10, 1000)

    # Evolve the system
    opts = Options(store_states=True)

    result = mesolve(
        H, psi0, tlist,
        c_ops=[],
        e_ops=[sigmax(), sigmay(), sigmaz()],
        options=opts
    )



    # Calculate the probability of being in the ground state  
    P0 = expect(basis(2,0) * basis(2,0).dag(), result.states)
    
    # plot probablity of being in ground state
    plt.plot(tlist, P0, label=f'Δ = {Delta}')

plt.xlabel("Time")
plt.ylabel("P(|0⟩)")
plt.title('Probability of being in the ground state')
plt.legend()

# save the plot
plt.savefig(f'prob_ground.png')