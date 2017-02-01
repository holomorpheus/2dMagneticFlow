#############################################################
##                                                         ##
##    Python script by:                                    ##
##    Gabriel Martins, on 11/25/2015                       ##
##                                                         ##
##    Plots orbits of different magnetic fields in the     ##
##    unit disc given in polar coordinates.                ##
##                                                         ##
#############################################################

#-----------------------------------------------------------------
# Imports
import numpy as np
import matplotlib.pyplot as plt
import scipy.integrate as scp
#-----------------------------------------------------------------

#-----------------------------------------------------------------
# Define magnetic field B
def B(r):
  #x, y = r[0]*np.cos(r[1]), r[0]*np.sin(r[1])
  
  #return r[0]*np.cos(r[1])/(1-r[0])**2 + r[0]*np.sin(r[1])/(1-r[0])**3
  
  # Fig 1
  return r[0]/(1-r[0])
  
  # Fig 2a
  #return r[0]*(1./(1-r[0]) + 7*y + 5*x**2)
  
  # Fig 2b  
  #return r[0]*(1./(1-r[0]) + 10*x - 2*x**2 - 10*y**3) 
  
  # Fig 3
  #return r[0]/(1-r[0])**0.5
  
# Define callable for the vector field in phase space
def f(v, t):
    r, dr = v[:2], v[2:]
    Jpol = np.array([-dr[1],dr[0]/r[0]**2])
    quad = np.array([r[0]*(dr[1]**2),-2*dr[0]*dr[1]/r[0]])
    ddr = -B(r)*Jpol+quad
    return np.hstack((dr, ddr))
#-----------------------------------------------------------------

#-----------------------------------------------------------------
# Integrating and plotting    

# Creates figure and axis
fig, ax = plt.subplots()

ax.set_xlim((-1.1,1.1))
ax.set_ylim((-1.1,1.1))
ax.set_aspect('equal')

# Plot boundary unit circle in blue
theta = np.linspace(0.,2*np.pi,128)
cs=np.zeros((128,2))
cs[:,0], cs[:,1] = np.cos(theta), np.sin(theta)
ax.plot(cs[:,0], cs[:,1], 'b-') # path

# Integrating and plotting function

def plot(r0,tmax,grid,color):
  tspan = np.linspace(0.0, tmax, grid)  
  rs = scp.odeint(f, r0, tspan)
  xs=rs.copy()
  xs[:,0], xs[:,1] = rs[:,0]*np.cos(rs[:,1]), rs[:,0]*np.sin(rs[:,1])
  ax.plot(xs[0,0], xs[0,1], color+'o')
  ax.plot(xs[:,0], xs[:,1], color+'-')

#-----------------------------------------------------------------

#-----------------------------------------------------------------
# Fig 1

## Plots first orbit, r0 = 0.7, in green
#r0 = [0.7,np.pi/2,1.,0.]
#tmax = 7*np.pi-2.
#grid = 1024
#color = 'g'
#plot(r0,tmax,grid,color)
#
## Plots second orbit, r0 = 0.5, in purple
#r0 = [0.5,np.pi/2,1.,0.]
#tmax = 12*np.pi-1.8
#grid = 2048
#color = 'm'
#plot(r0,tmax,grid,color)
#-----------------------------------------------------------------

#-----------------------------------------------------------------
# Fig 2a

# Plots orbit, r0 = 0.8, in purple
#r0 = [0.8,np.pi/2,1.,0.]
#tmax = 12*np.pi
#grid = 4096
#color = 'm'
#plot(r0,tmax,grid,color)
#-----------------------------------------------------------------

#-----------------------------------------------------------------
# Fig 2b

## Plots orbit, r0 = 0.7, in purple
#r0 = [0.7,np.pi/2,1.,0.]
#tmax = 8*np.pi
#grid = 4*1024
#color = 'm'
#plot(r0,tmax,grid,color)
#-----------------------------------------------------------------

#-----------------------------------------------------------------
# Fig 3

## Plots trapped orbit, r0 = 0.5, in purple
r0 = [0.7,np.pi/2,.5,0.]
tmax = 24*np.pi-0.1
grid = 2048
color = 'm'
plot(r0,tmax,grid,color)
plot(r0,-.6,grid,color)
#
## Plots escaping orbits, r0 = 0.7, in green
#tmax = 7*np.pi+1
#grid = 1024

tmax = 40*np.pi+1
grid = 2048

color = 'g'
r0 = [0.7,np.pi/2,1.,0.]
plot(r0,tmax,grid,color)
plot(r0,-tmax,grid,color)
r0 = [0.7,3*np.pi/2,1.,0.]
plot(r0,tmax,grid,color)
plot(r0,-tmax,grid,color)
#-----------------------------------------------------------------

#-----------------------------------------------------------------
# Experiments

# Plots orbit, r0 = 0.8, in purple
#r0 = [0.9,np.pi/3,1.,0.]
#tmax = 60
#grid = 4096
#color = 'm'
#plot(r0,tmax,grid,color)
#-----------------------------------------------------------------