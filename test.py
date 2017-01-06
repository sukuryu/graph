import matplotlib.pyplot
import numpy
import matplotlib.animation as animation
import matplotlib.pyplot as plt
import math
from mpl_toolkits.mplot3d import Axes3D
import tcp_server

def update_plot(i):
    datalist = server.get_pitch_etc()

    if datalist == [] or type(datalist[0]) == str or type(datalist[1]) == str or type(datalist[2]) == str :
        datalist = [1, 1, 1]

    #受信データから行列作成
    R = numpy.array([[numpy.cos(datalist[1]) * numpy.cos(datalist[2]),
                -numpy.cos(datalist[1]) * numpy.sin(datalist[2]),
                 numpy.sin(datalist[1])],
                [numpy.sin(datalist[0]) * numpy.sin(datalist[1]) * numpy.cos(datalist[2]) + numpy.cos(datalist[0]) * numpy.sin(datalist[2]),
                 -numpy.sin(datalist[0]) * numpy.sin(datalist[1]) * numpy.sin(datalist[2]) + numpy.cos(datalist[0]) * numpy.cos(datalist[2]),
                 -numpy.sin(datalist[0]) * numpy.cos(datalist[1])],
                [-numpy.cos(datalist[0]) * numpy.sin(datalist[1]) * numpy.cos(datalist[2]) + numpy.sin(datalist[0]) * numpy.sin(datalist[2]),
                 numpy.cos(datalist[0]) * numpy.sin(datalist[1]) * numpy.sin(datalist[2]) + numpy.sin(datalist[0]) * numpy.cos(datalist[2]),
                 numpy.cos(datalist[0]) * numpy.sin(datalist[1])]])

    init_position = numpy.array(init_position_3d)

    #内積
    current_coordinates = numpy.dot(R, init_position)

    x = numpy.array([1, 1 - current_coordinates[0]])
    y = numpy.array([1, 1 + current_coordinates[1]])
    z = numpy.array([1, 1 + current_coordinates[2]])

    plt.cla()

    ax.set_xlim(0, 2)
    ax.set_ylim(0, 2)
    ax.set_zlim(0, 2)

    ax.scatter3D(x, y, z)

    #im = ax.plot(test, test, test, "o", color="#cccccc", ms = 15)
    #im = ax.plot(current_coordinates, current_coordinates, current_coordinates, "o", color="#ff00cc", ms = 10)

mode = "all_elev"
server = tcp_server.tcp_server("0.0.0.0", 7000)
server.create_server()
server.accept_and_start(mode)
init_position_3d = [1, 0, 0]

fig = plt.figure()

ax = Axes3D(fig)

ani = animation.FuncAnimation(fig, update_plot, interval = 100)

plt.show()
