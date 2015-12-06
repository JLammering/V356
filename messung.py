import numpy as np

L = 1.217e-3
C1 = 20e-9#20.13e-9
C2 = 10e-9#9.41e-9

Z = np.sqrt(2*1.217e-3/(9.41e-9+20.13e-9))
print('Z(omega)=  ', Z)

omega1 = np.sqrt(2/(L * C1))
print('omega1 =', omega1)

omega2 = np.sqrt(2/(L * C2))
print('omega2 =', omega2)

omega3 = np.sqrt((2*(C1+C2))/(L*C1*C2))
print('omega3 =', omega3)

nu1 = omega1/(2* np.pi)
print('nu1 =',nu1)

nu2 = omega2/(2* np.pi)
print('nu2 =',nu2)

nu3 = omega3/(2* np.pi)
print('nu3 =',nu3)
