from pysces import *
#from vortex import *
import matplotlib.pyplot as plt
from matplotlib.mlab import psd
import numpy as np
from numpy import *
from pylab import *

angle = 0
airfoil = naca_airfoil("0012", 200, zero_thick_te=True)  
#airfoil = TransformedBody(airfoil, displacement=(-0.25, 0))
airfoil = TransformedBody(airfoil, angle)
bound = BoundVortices(airfoil)

num_steps = 300
Uinfty = (1,0)
dt = 0.01
Vortices.core_radius = dt

#free vortices

v1	=	(-2, 0.1)
s1	=	1.810137
c1 =   0.1
vort = Vortices([v1],[s1])

flow = ExplicitEuler(dt, Uinfty, bound, wake=vort, need_force='wake_impulse')
#flow = ExplicitEuler(dt, Uinfty, bound, wake=vort, need_force='airfoil')

for i in range(1,num_steps):
    flow.advance()
    q1 = flow.wake.positions
    plt.plot(q1[:,0], q1[:,1], 'ro')
#    plt.plot(q2[:,0], q2[:,1], 'bo')
#    plt.plot(q3[:,0], q3[:,1], 'go')
plt.axis('equal')
plt.grid(True)
plt.show()
#plot force
f = flow.force
steps = np.arange(0, num_steps*dt, dt)
expected_Cl = (np.pi * np.pi / 90) * angle
expected = np.array([expected_Cl, expected_Cl])
steps2 = np.array([0, num_steps*dt])

#saving data
data = (steps, 2*f[:,0])  
# savetxt('Tu_038_GA.csv',np.column_stack((steps, 2*f[:,1])), fmt='%5s', delimiter=',')

fig = plt.figure()
ax1 = fig.add_subplot(111)
ax1.plot(steps, 2*f[:,0], c='b', label='Cd')
ax1.plot(steps, 2*f[:,1], c='r', label='Cl')
ax1.plot(steps2, expected, c='g', label='expected Cl')
plt.legend();
plt.xlabel('time')
#plt.grid(True)
# plt.savefig('Tu_038_GA.pdf')
plt.show()



average_thrust = np.average(flow.force[:,0])
#print average_thrust

average_lift = np.average(flow.force[:,1])
#print average_lift

def Curles_loadingNoise(y_int,c_sound,r_dist,L,dt,Velo):
	p_acoustic = ((y_int*L)/(4*np.pi*dt*c_sound*(r_dist**2)))*(0.5*1.225*pow(Velo,2))
	return p_acoustic

noise = Curles_loadingNoise(1, 343, 3, 2*f[:,1],dt,1)
#print noise
def L_p(x):
	return 20*np.log10(np.abs(x)/2.e-5)

(werte,freq) = psd(noise,Fs=1/dt,detrend='mean')
pegel=L_p(werte)
plt.figure(2)
plt.semilogx(freq,pegel,label='v')
plt.legend()
plt.show()