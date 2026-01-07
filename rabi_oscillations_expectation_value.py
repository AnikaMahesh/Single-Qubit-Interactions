import numpy as np
import matplotlib.pyplot as plt
from qutip import *

# Parameters
hbar = 1.0        # we can set ħ = 1 in natural units
Omega = 1.0       # Rabi frequency



plt.figure()
for Delta in [0, 0.2, 0.4]:   # detuning

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

    # Get expectation values
    ex, ey, ez = result.expect

    # Plot Bloch components
    plt.figure()
    plt.plot(tlist, ex, label='⟨σx⟩')
    plt.plot(tlist, ey, label='⟨σy⟩')
    plt.plot(tlist, ez, label='⟨σz⟩')
    plt.xlabel('Time')
    plt.ylabel('Expectation value')
    plt.legend()
    plt.title(f'Rabi Oscillations in the Rotating Frame when Δ = {Delta}')

    plt.savefig(f'rabi_oscillations_{Delta}.png')
    plt.close()