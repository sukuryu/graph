from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import numpy
import tcp_server
import math

mode = "all_elev"
server = tcp_server.tcp_server("0.0.0.0", 7000)
server.create_server()
server.accept_and_start(mode)
init_position_3d = [1, 0, 0]

while True:
    datalist = server.get_pitch_etc()

    if datalist == [] or len(datalist) != 3 or type(datalist[0]) != float:
        continue

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
    



#fig = plt.figure()
#ax = Axes3D(fig)

#ax.set_xlim(0, 2)
#ax.set_ylim(0, 2)
#ax.set_zlim(0, 2)

#test = numpy.array([1, 1, 1])
#rad = numpy.radians(45)
#test2 = numpy.array([1 + numpy.cos(rad), 1 + numpy.sin(rad), 1 + numpy.sin(rad)])

#ax.plot(test, test, test, "o", color="#cccccc", ms = 15)

#ax.plot(test2, test2, test2, "o", color="#ff00cc", ms = 10)

#plt.show()
