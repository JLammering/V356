import matplotlib.pyplot as plt
import numpy as np

C1 = 20 * 10**(-9)
C2 = 10 * 10**(-9)
L = 1.217 * 10**(-3)

t = np.linspace(0, np.pi/2, 1000)
plt.plot(t, np.sqrt((1/L)*((1/C1) + (1/C2)) + (1/L)* np.sqrt(((1/C1) + (1/C2))**2 - (4*(np.sin(t))**2)/(C1*C2))), 'r',  label = r'$\omega_2$')

a = np.linspace(0, np.pi/2, 1000)
b = np.linspace(0, np.pi/2, 1000)

m = np.sqrt((1/L)*((1/C1) + (1/C2)) + (1/L)* np.sqrt(((1/C1) + (1/C2))**2 - (4*(np.sin(np.pi/2))**2)/(C1*C2)))
n = np.sqrt((1/L)*((1/C1) + (1/C2)) + (1/L)* np.sqrt(((1/C1) + (1/C2))**2 - (4*(np.sin(0))**2)/(C1*C2)))

plt.plot(a, 0*a + m,'b', label = r'$\omega_2(\frac{\pi}{2})$')
plt.plot(b, 0*b + n, 'k', label = r'$\omega_2(0)$')

plt.legend(loc = 'best')
plt.ylim(350000, 550000)
plt.xlim(0, np.pi/2, 1000)
plt.xlabel(r'$\theta$')
plt.ylabel(r'$\omega \:/\: \si{\hertz}$')
plt.grid()

print(m,n)
plt.savefig('build/plotw2.pdf')
