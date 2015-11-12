"""
Computational Neurodynamics
Exercise 1

Solves the ODE dy/dt=y (exact solution: y(t)=exp(t)), by numerical
simulation using the Euler method, for two different step sizes.

(C) Murray Shanahan et al, 2015
"""

import numpy as np
import matplotlib.pyplot as plt

m = 1
c = 0.1
k = 1
dt = 0.01  # Small integration step

# Create time points
Tmin = 0
Tmax = 100
T = np.arange(Tmin, Tmax+dt, dt)
y = np.zeros(len(T))
dydt2 = np.zeros(len(T))
dydt = np.zeros(len(T))

# Approximated solution with small integration Step
y[0] = 1  # Initial value
dydt[0] = 0
dydt2[0] = (-c/m)*dydt[0] - (k/m)*y[0]
for t in xrange(1, len(T)):
	dydt2[t] = (-c/m)*dydt[t-1] - (k/m)*y[t-1]
	dydt[t] = dydt[t-1] + dt*dydt2[t-1]
	y[t] = y[t-1] + dt*dydt[t-1]

# Plot the results
plt.plot(T, y, 'g', label='Q1')
plt.title('Question 1')
plt.xlabel('t')
plt.ylabel('y')
plt.legend(loc=0)
plt.show()


