import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

fig, ax = plt.subplots()
g=9.8
h=0.025

circle, = ax.plot([], [], 'bo', ms=8)
coord = np.array([6.,9.])
speed = np.array([5.,0.])

def init():
    ax.set_xlim([0., 20.])
    ax.set_ylim([0., 20.])
    return circle,

def updatefig(frame):
	speed[1] = speed[1]-h*g
	coord[1] = coord[1]-0.5*h*h*g+h*speed[1]
	if coord[1]<= 0.:
		speed[1]=-speed[1]

	speed[0] = speed[0]-h*0
	coord[0] = coord[0]+h*speed[0]

	if coord[0]<=0. or coord[0]>=20.:
		speed[0]=-speed[0]




	circle.set_xdata(coord[0])
	circle.set_ydata(coord[1])
	return circle,

anim = animation.FuncAnimation(fig, updatefig, frames=2000, init_func=init, interval=100, blit=True, repeat=False)

plt.show()
