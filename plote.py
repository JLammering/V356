import matplotlib.pyplot as plt
import numpy as np

L = 1.75e-3
C = 22e-9
#x, y = np.genfromtxt('d_1.txt', unpack = True)

def v_gr(nu):
    return (1/(np.sqrt(L*C)))*np.sqrt(1-0.25*L*C*(nu*2*np.pi)**2)

nu = np.linspace(0,100000,100000)

plt.plot(nu, v_gr(nu), 'b-', label = 'Theoriekurve')
plt.xlabel(r'$\nu \:/\: \si{\hertz}$')
plt.ylabel(r'$v_{gr} \:/\: \si{\meter\per\second}$')
plt.legend(loc = 'best')


plt.tight_layout(pad=0, h_pad=1.08, w_pad=1.08)
plt.savefig('build/plote.pdf')
