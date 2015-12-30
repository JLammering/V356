import matplotlib.pyplot as plt
import numpy as np

#Messwerte umrechnen
x, y = np.genfromtxt('c.txt', unpack = True)
y = y *  1/32

#abspeichern
np.savetxt('build/vph.txt', [x*2*np.pi, (x/y)/1000, y])
plt.plot((x *2* np.pi)/1000, (x/y)/1000, 'k.', label = r'$Messwerte$')

#Werte
L = 1.75 *10**(-3)
C = 22 *10**(-9)

#Theorie
w = np.linspace(1, 3000000, 100000)
plt.plot(w/1000, (w/(np.arccos(1-0.5*L*C*(w)**2)))/1000, label = r'$Theoriekurve$')

#Grenzwert
x = np.linspace(1, 320000)
plt.plot(x/1000, (0*x + 1/np.sqrt(L*C))/1000, label = r'$Grenzwert$')

plt.xlim(0, 320)
plt.xlabel(r'$\omega \:/\: \si{\kilo\hertz}$')
plt.ylabel(r'$v_{\text{Ph}} \:/\: \si{\kilo\meter\per\second}$')
plt.legend(loc = 'best')

plt.savefig('build/plotvph.pdf')
