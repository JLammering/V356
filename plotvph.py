import matplotlib.pyplot as plt
import numpy as np


x, y = np.genfromtxt('c.txt', unpack = True)
y = y* np.pi * 1/32
plt.plot(x, x/y, 'k.')

L = 1.75 *10**(-3)
C = 22 *10**(-9)
w = np.linspace(1, 3000000, 100000)
plt.plot(w/(2*np.pi), w/(2*np.pi)/(np.arccos(1-0.5*L*C*(w/(2*np.pi))**2)))
x = np.linspace(1, 320000 )
plt.plot(x, 0*x + 1/np.sqrt(L*C))
plt.xlim(0, 320000)


plt.savefig('build/plotvph.pdf')
