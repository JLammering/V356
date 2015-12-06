import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import linregress

x, y = np.genfromtxt('datenlinreg.txt', unpack = True)

slope, intercept, r_value, p_value, std_err = linregress(x, np.log(y))
a = np.linspace(0, 100000, 100000)
plt.plot(a, slope*a + intercept, 'r-', label = r'$Ausgleichsgerade$')
plt.xlim(0,50)
plt.ylim(0,20)

plt.plot(x, np.log(y), 'bx')

print('m = ', slope, 'b = ', intercept, 'r^2 = ', r_value**2, 'Fehler = ', std_err)

plt.savefig('build/linregplot.pdf')
