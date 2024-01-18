# -*- coding: utf-8 -*-
"""
Created on Mon Jan  2 21:05:53 2023

@author: Calum
"""

import numpy as np
import matplotlib.pyplot as plt
#matplotlib inline

# Model parameters
M = 0.045 # Mass of projectile in kg
g = 9.8 # Acceleration due to gravity (m/s^2)
V = 74.65568 # Initial velocity in m/s
ang = 10.9 # Angle of initial velocity in degrees
Cd = 0.000 # Drag coefficient
dt = 0.5 # time step in s

# You can check the variables by printing them out
print (V, ang)

# Set up the lists to store variables
# Initialize the velocity and position at t=0
t = [0] # list to keep track of time
vx = [V*np.cos(ang/180*np.pi)] # list for velocity x and y components
vy = [V*np.sin(ang/180*np.pi)]
x = [0] # list for x and y position
y = [0]

# Drag force
drag=Cd*V**2                # drag force

# Acceleration components
ax = [-(drag*np.cos(ang/180*np.pi))/M ]
ay = [-g-(drag*np.sin(ang/180*np.pi)/M) ]

## Leave this out for students to try
# We can choose to have better control of the time-step here
dt = 0.0002

# Use Euler method to update variables
counter = 0
while (y[counter] >= 0): # Check that the last value of y is >= 0
 t.append(t[counter]+dt) # increment by dt and add to the list of time

 # Update velocity
 vx.append(vx[counter]+dt*ax[counter]) # Update the velocity
 vy.append(vy[counter]+dt*ay[counter])
 
 # Update position
 x.append(x[counter]+dt*vx[counter])
 y.append(y[counter]+dt*vy[counter])
 
 # With the new velocity calculate the drag force and update acceleration
 vel = np.sqrt(vx[counter+1]**2 + vy[counter+1]**2) # magnitude of velocity
 drag = Cd*vel**2 # drag force
 ax.append(-(drag*np.cos(ang/180*np.pi))/M)
 ay.append(-g-(drag*np.sin(ang/180*np.pi)/M))
 
 # Increment the counter by 1
 counter = counter +1

# Let's plot the trajectory
plt.plot(x,y,'ro')
plt.ylabel("y (m)")
plt.xlabel("x (m)")

# The last value of x should give the range of the projectile approximately.

print ("Range of projectile is {:3.1f} m".format(x[counter]))