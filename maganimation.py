#-----------------------------------------------------------------
# Imports
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as ani

#-----------------------------------------------------------------

#-----------------------------------------------------------------
# Charge array

q = np.load('chargeq.npy')
t = np.load('charget.npy')
grid=len(t)
dt = t[1] - t[0]
fpsec = int(1/dt)
#-----------------------------------------------------------------

#-----------------------------------------------------------------
# Animating    

# Creates figure and axis
fig, ax = plt.subplots()

# Axis setup
ax.set_xlim((-1.2,1.2))
ax.set_ylim((-1.2,1.2))
ax.set_frame_on(False)
ax.axes.get_xaxis().set_visible(False)
ax.axes.get_yaxis().set_visible(False)
ax.set_aspect('equal')
# Legends
ax.set_title(r'$ B = \frac{1}{(1-r)^2} + 2\cos(x^2) - 10\sin(y^3))$')
time_text = ax.text(0.00, 0.90, '', transform=ax.transAxes)

# Making a circle
theta = np.linspace(0.,2*np.pi,128)
ct=np.zeros((128,2))
ct[:,0], ct[:,1] = 1.02*np.cos(theta), 1.02*np.sin(theta)
circle, = ax.plot(ct[:,0], ct[:,1], 'k-', lw=2, alpha=0.7)

# Point and line
line, = ax.plot([], [], 'b-', lw=2, alpha=0.3)
point, = ax.plot([], [], 'mo')

# initialization function: plot the background of each frame
def init():
    line.set_data([], [])
    point.set_data([], [])
    return line, point

# animation function.  This is called sequentially
def animate(i):
    time_text.set_text('time = %.1f' % t[i])
    line.set_data(q[:i+1,0],q[:i+1,1])
    point.set_data(q[i,0],q[i,1])
    return line, point

#plt.rcParams['animation.ffmpeg_path']='C:/ffmpeg/bin/ffmpeg.exe'
writer=ani.FFMpegWriter(bitrate=5000, fps=fpsec)
# call the animator.  blit=True means only re-draw the parts that have changed.
anim = ani.FuncAnimation(fig, animate, init_func=init,
                               frames=grid, interval=20, blit=True)

anim.save('tempani.mp4', writer=writer)

plt.close(fig)
#-----------------------------------------------------------------

