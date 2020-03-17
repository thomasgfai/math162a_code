#!/usr/bin/python
import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import ode
from math import *

# Function
def f(t,y,arg1):
    return [998*y[0]+1998*y[1],-999*y[0]-1999*y[1]]

# Initial conditions
yinit=[1,0]

# Set up stiff integrator and parameters
r=ode(f).set_integrator('zvode', method='bdf')
r.set_initial_value(yinit,0).set_f_params(2.0).set_jac_params(2.0)
dt=0.05

tvec = []
ex1vec = []
ex2vec = []
y1vec = []
y2vec = []

# Loop while the time is less than 2
while r.successful() and r.t<2:
    r.integrate(r.t+dt)

    # Print solution and comparison with exact answer
    ex1=2*exp(-r.t)-exp(-1000*r.t)
    ex2=-exp(-r.t)+exp(-1000*r.t)
    #print r.t,float(r.y[0]),float(r.y[1]),ex1,ex2,float(r.y[0])-ex1,float(r.y[1])-ex2

    tvec.append(r.t) 
    ex1vec.append(ex1)
    ex2vec.append(ex2)
    y1vec.append(r.y[0])
    y2vec.append(r.y[1])

# Plot the results
plt.plot(tvec,ex1vec,'.',tvec,y1vec,'-')
plt.legend(['exact','odeint'],loc='best')
plt.show()

# Plot the results
plt.plot(tvec,ex2vec,'.',tvec,y2vec,'-')
plt.legend(['exact','odeint'],loc='best')
plt.show()
