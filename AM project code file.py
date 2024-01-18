# -*- coding: utf-8 -*-
"""
Created on Thu Jan 12 22:32:37 2023

@author: Calum
"""

import math
import matplotlib.pyplot as plt

#parameters = { mass , c , ro(air density) , g , initial velocity v0 }

ro=1.25    #Air density
c=0.024       #Drag coefficient
r=0.0427/2    #radius ball
area=(math.pi*r**2) #Area ball
mass=0.0459  #Mass of ball
dt=0.01    #time interval
v0=7*2.2360679775       #Starting velocity
angle=45   #Starting angle, in degrees
g=9.81       #Gravity     

theta=math.radians(angle)   #angle in radians

#fn to calculate the velocity
def vel(vx,vy): #velocity
    v=math.sqrt(vx**2+vy**2)
    return v

#Function to calculate aero-drag
def DE(ro,area,v):   
    DD=float((ro*area*c*(v**2))/2)
    return DD

#projectile motion

# tr=0 for projectile without drag
# tr=1 for projectile with drag

def projectile(v0,ro,area,tr):
    t=0
    p=0
    x=[0]
    y=[0]
    accel_x=[]
    accel_y=[]
    velocity = []
    
    vy=[v0*math.sin(theta)] 
    vx=[v0*math.cos(theta)]

    while y[p]>=0:
        vxx=float(vx[p])
        vyy=float(vy[p]) 
        
        v=vel(vxx,vyy)
        velocity.append(v)
        D = tr*DE(ro,area,v)  # D in eqn
        
        theta2 = math.atan(vyy/vxx)
        
        Fx=-D*math.cos(theta2)
        Fy=-mass*g-D*math.sin(theta2)
        
        ax=Fx/mass
        ay=Fy/mass

        accel_x.append(ax)
        accel_y.append(ay)

        delta_x=(vxx*dt)+(accel_x[p]*(dt**2)/2) 
        delta_y=(vyy*dt)+(accel_y[p]*(dt**2)/2)
        
        vx.append(vxx+((accel_x[p])*dt))
        vy.append(vyy+((accel_y[p])*dt))

        x.append(x[p]+delta_x) 
        y.append(y[p]+delta_y) 

        t+=dt
        p+=1
    
    return x, y, t, v

#######################################

x1, y1, t1, v1 = projectile(v0,ro,area,1)
x2, y2, t2, v2 = projectile(v0,ro,area,0)

#############   Graph  ################
try: 
    print("\nWith drag stats:")
    print("Range with drag is ",round(x1[-1],2))
    print("Total time of flight ",round(t1,2),"s")

    print("\nWithout drag stats")
    print("Range without drag is ",round(x2[-1],2))
    print("Total time of flight without drag",round(t2,2),"s")
    
    fig, ax = plt.subplots(1, 1)
    plt.title("Projectile motion")
    ax.set_xlim(0, 25.5)
    ax.set_ylim(0, 7)
    #ax.plot(x1,y1,'b-',label='With drag')
    ax.plot(x2,y2,'g-',label='without drag')
    plt.grid()
    ax.legend()
    plt.ylabel("Y Coordinate")
    plt.xlabel("X Coordinate : Horizontal")
    plt.show()

except: 
    print("Check the inputs and Try again!!!!")