# -*- coding: utf-8 -*-
"""
Created on Mon Jan  9 21:31:15 2023

@author: Calum
"""

import math
import matplotlib.pyplot as plt

#parameters = { mass , c , ro(air density) , g , initial velocity v0 }

ro=1.225
c=0.5
r=0.0366
area=(math.pi*r*r)
mass=0.145
dt=0.001     #time interval
v0=50
angle=30
g=9.8        

theta=math.radians(angle)   #angle in radians

#fn to calculate the velocity
def vel(vx,vy): #velocity
    v=math.sqrt(vx**2+vy**2)
    return v

def DE(ro,area,v):   # drag 
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
    
    vy=[v0*math.sin(theta)] 
    vx=[v0*math.cos(theta)]

    while y[p]>=0:
        vxx=float(vx[p]) 
        vyy=float(vy[p]) 
        v=vel(vxx,vyy)
        D = tr*DE(ro,area,v)  # D in eqn
        ay=-g-((D/mass)*vyy)
        ax=-(D/mass)*vxx  

        accel_x.append(ax)
        accel_y.append(ay)

        delta_x=(vxx*dt)+(accel_x[p]*(dt**2)/2) 
        delta_y=(vyy*dt)+(accel_y[p]*(dt**2)/2)
        
        vx.append(vxx+((accel_x[p])*dt))
        vy.append(vyy+((accel_y[p])*dt))

        x.append(x[p]+delta_x) 
        y.append(y[p]+delta_y) 

        t=t+dt
        p=p+1
    
    return x, y, t

#######################################

x1, y1, t1 = projectile(v0,ro,area,1)
x2, y2, t2 = projectile(v0,ro,area,0)

#############   Graph  ################
try: 
    print("\nWith drag stats:")
    print("Range with drag is ",round(x1[-1],2))
    print("Total time of flight ",round(t1,2),"s")

    print("\nWithout drag stats")
    print("Range without drag is ",round(x2[-1],2))
    print("Total time of flight without drag",round(t2,2),"s")

    plt.title("Projectile motion")
    plt.plot(x1,y1,'r-',label='With drag')
    plt.plot(x2,y2,'g-',label='without drag')
    plt.grid()
    plt.legend()
    plt.ylabel("Y Coordinate")
    plt.xlabel("X Coordinate")
    plt.show()

except: 
    print("Check the inputs and Try again!!!!")