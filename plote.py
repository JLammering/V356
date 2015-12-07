import matplotlib.pyplot as plt
import numpy as np

x, y = np.genfromtxt('e.txt', unpack = True)

plt.plot(x, y, 'rx', label = 'Messpunkte')
plt.xlabel(r'Kettenglied')
plt.ylabel(r'$U \:/\: \si{\volt}$')
plt.legend(loc = 'best')
plt.title(r'gemessen beim ersten Maximum : f = 5040 Hz mit Abschlusswiderstand = Wellenwid.')


plt.tight_layout(pad=0, h_pad=1.08, w_pad=1.08)
plt.savefig('build/plote.pdf')
