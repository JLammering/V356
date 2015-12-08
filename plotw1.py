# Dispersionskurve Für w1, untere Frequenzkurve
# Kreisfrequenz w1 gegen Phasenverschiebung t
# a ist erste Grenzfrequenz
# Aufgetragene Messwerte

import matplotlib.pyplot as plt
import numpy as np

# Messwerte:
y, x = np.genfromtxt('b1.txt', unpack = True)
x = np.pi*x/32
y = 2*np.pi*y
plt.plot(x, y, 'k.', label = r'$Messwerte$')

# Werte:
C1 = 20 * 10**(-9)
C2 = 10 * 10**(-9)
L = 1.217 * 10**(-3)

# Dispersionskurve:
t = np.linspace(0, np.pi/2, 1000)
plt.plot(t, np.sqrt((1/L)*((1/C1) + (1/C2)) - (1/L)*np.sqrt(((1/C1) +
(1/C2))**2 - (4*(np.sin(t))**2)/(C1*C2))), 'r', label = r'$\omega_1$')

# Grenzfrequenz:
m = np.sqrt((1/L)*((1/C1) + (1/C2)) - (1/L)*np.sqrt(((1/C1) + (1/C2))**2 -
(4*(np.sin(np.pi/2))**2)/(C1*C2)))
a = np.linspace(0, np.pi, 1000)
plt.plot(a, 0*a + m,'k', label = r'$\omega_1(\frac{\pi}{2})$')

plt.legend(loc = 'best')
plt.ylim(0, 400000)
plt.xlim(0, np.pi/2, 1000)
plt.xlabel(r'$\theta$')
plt.ylabel(r'$\omega \:/\: \si{\hertz}$')
plt.grid()

print(m, np.sqrt(2/(L*C1)))
plt.savefig('build/plotw1.pdf')
