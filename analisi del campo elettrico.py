import numpy as np
from scipy import linalg
from scipy.sparse import diags
from matplotlib import pyplot as plt

N = 100
L = 1
x1 = 0.3
x2 = 0.6

x = np.linspace(0, L, N)
e_r = np.where((x<x1) | (x>x2), 1.0, 80)

d = 2 / e_r
d_sup = -1 / e_r[1:]
d_inf = -1 / e_r[:-1]

M = diags([d, d_sup, d_inf], offsets = [0,1,-1]).toarray()
eg_val, eg_vect = linalg.eigh(M)



for i in range(4):
    plt.plot(x, eg_vect[:,i], label = f"Modo {i+1}")



plt.legend()
plt.title("Ricostruzione del campo con modi normali")
plt.xlabel("Posizione x")
plt.ylabel("Modo normale E")
plt.axvline(0, color='gray', linewidth=2)
plt.axvline(L, color='gray', linewidth=2)
plt.axvspan(x1, x2, color='lightblue', alpha=0.4, label='Dielettrico')
plt.grid(True)
plt.show()
