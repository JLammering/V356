import matplotlib.pyplot as plt
import numpy as np


x = np.genfromtxt('c.txt', unpack = True)
L = 1.75 *10**(-3)
C = 22 *10**(-9)
w = np.linspace(0.00001, 0.04, 100000)
plt.plot(w, w/(np.arccos(1-0.5*L*C*w**2)))

plt.savefig('build/plotvph.pdf')
