import time
import math as math
import matplotlib.pyplot as plt
import numpy as np

__author__ = 'mrasquinha'



def find_slope(xdata, ydata):
    xdatalog = []
    ydatalog = []

    for a in range(len(xdata)):
        xdatalog.append(math.log(xdata[a]))
        try:
            ydatalog.append(math.log(ydata[a]))
        except ValueError:
            ydatalog.append(0)
    print "Slope of log log plot (b) = ", (ydatalog[7]-ydatalog[4])/(xdatalog[7]-xdatalog[4])

    # fig = plt.figure()
    # plt.plot(xdata, ydata)
    # plt.xscale('log',basex=2)
    # plt.yscale('log',basey=2)
    # plt.show(block=True)


#Problem1
data=np.array([[4096,0.000], [8192,0.000],
[16384,0.001],
[32768,0.003],
[65536,0.007],
[131072,0.018],
[262144,0.048],
[524288,0.124],
[1048576,0.325],
[2097152,0.850],
[4194304,2.218],
[8388608,5.790],
[16777216,15.120],
[33554432,39.490],
[67108864,103.076],
[134217728,269.141],
[268435456,702.751],
[536870912,1834.917]])
xdata = data[:,0]
ydata = data[:,1]
find_slope(xdata, ydata)


# problem 2: run time analysis
xdata=[]
ydata=[]
N=2
while (N<1024):
    start_time = time.time()

    sum = 0
    for i in range(N):
        for j in range(i*i):
            for k in range (j*j):
                sum += 1


    elapsed_time = time.time() - start_time
    xdata.append(N)
    try:
        ydata.append(elapsed_time)
    except ValueError:
        ydata.append(0)

    print("%04d\t%0.2f"% (N, elapsed_time))
    N = N*2

find_slope(xdata, ydata)