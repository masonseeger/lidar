'''Animates distances and measurment quality'''
from rplidar import RPLidar
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.animation as animation

PORT_NAME = '\\\\.\\com4'
DMAX = 6000 #max distance in cm
IMIN = 0
IMAX = 50

def update_line(num, iterator, line):
    scan = next(iterator)
    offsets = np.array([(np.radians(meas[1]), meas[2]) for meas in scan]) #Where the dot is placed from the origin
    line.set_offsets(offsets) # setting the new dot
    intens = np.array([meas[0] for meas in scan])

    line.set_array(intens) # sets the image array
    return line,

def run():
    lidar = RPLidar(PORT_NAME)
    fig = plt.figure()
    ax = plt.subplot(111, projection='polar')
    line = ax.scatter([0, 0], [0, 0], s=15, c=[0,0],
                         lw=0) # this is basically initializing the dots that we will be drawing
                           #initially at 0,0 at size 5 with color[] and linewidth 0
    ax.set_rmax(DMAX) #set the max radius
    ax.grid(True)

    iterator = lidar.iter_scans()
    ani = animation.FuncAnimation(fig, update_line,
        fargs=(iterator, line), interval=25)
    plt.show()
    lidar.stop()
    lidar.stop_motor()
    lidar.disconnect()

if __name__ == '__main__':
    run()
