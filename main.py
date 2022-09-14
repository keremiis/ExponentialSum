from matplotlib import pyplot as plt
import math
import imageio
import os

def forward(m,d,y):
    N = 2*math.lcm(m, d, y) + 1
    values=[]
    fc=0
    sc=0
    for i in range(N):
        i=float(i)
        firstCoordinate=math.cos(2*math.pi*(i/m+i*i/d+i*i*i/y))
        secondCoordinate=math.sin(2*math.pi*(i/m+i*i/d+i*i*i/y))
        fc+=firstCoordinate
        sc+=secondCoordinate
        values.append((fc,sc))
    return values

def plotit(m,d,y):
    arr=forward(m,d,y)
    x = []
    y = []
    for elem in arr:
        x.append(elem[0])
        y.append(elem[1])
    plt.plot(x,y)
    plt.show()


def makegif(m,d,y):
    arr=forward(m,d,y)

    x = []
    y = []
    for elem in arr:
        x.append(elem[0])
        y.append(elem[1])

    for i in range(len(x)):
        xTemp = x[:i]
        yTemp = y[:i]
        plt.plot(xTemp, yTemp, color="c")
        filename = "plot" + str(i) + ".png"
        plt.savefig(filename)

    filenames=[]
    for i in range(len(arr)):
        filename = "plot" + str(i) + ".png"
        filenames.append(filename)
    with imageio.get_writer('mygif.gif', mode='I') as writer:
        for filename in filenames:
            image = imageio.v3.imread(filename)
            writer.append_data(image)
    filenames.remove("plot" + str(len(arr)-1) + ".png")

    for filename in set(filenames):
        os.remove(filename)

plotit(9,14,22)
