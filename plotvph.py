import matplotlib.pyplot as plt
import numpy as np


x, y = np.genfromtxt('c.txt', unpack = True)
y = y *  1/32
plt.plot(x *2* np.pi, x/y, 'k.', label = r'$Messwerte$')

L = 1.75 *10**(-3)
C = 22 *10**(-9)
w = np.linspace(1, 3000000, 100000)
plt.plot(w, w/(np.arccos(1-0.5*L*C*(w)**2)), label = r'$Theoriekurve$')
x = np.linspace(1, 320000)
plt.plot(x, 0*x + 1/np.sqrt(L*C), label = r'$Grenzwert$')
plt.xlim(0, 320000)
plt.xlabel(r'$\omega \:/\: \si{\hertz}$')
plt.ylabel(r'$v_{\text{Ph}} \:/\: \si{\meter\per\second}$')
plt.legend(loc = 'best')

plt.savefig('build/plotvph.pdf')
