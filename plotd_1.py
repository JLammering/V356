import matplotlib.pyplot as plt
import numpy as np

x, y = np.genfromtxt('d_1.txt', unpack = True)

plt.plot(x, y, 'rx', label = 'Messpunkte')
plt.xlabel(r'Kettenglied')
plt.ylabel(r'$U \:/\: \si{\volt}$')
plt.legend(loc = 'best')
plt.title(r'gemessen beim ersten Maximum f = \SI{5040}{\hertz}')


plt.tight_layout(pad=0, h_pad=1.08, w_pad=1.08)
plt.savefig('build/plotd_1.pdf')
