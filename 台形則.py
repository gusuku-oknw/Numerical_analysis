import matplotlib
import matplotlib.pyplot as plot
from math import *


def f(x):
    return sin(x)


def xi(i, xs, xe, ndiv):
    return xs*(ndiv-i)/ndiv + xe * i/ndiv


def draw(a, b, N):
    fig = plot.figure()
    graph = fig.add_subplot()
    graph.set_xlim(a, b)

    px = []; py = []; M = 1000
    for i in range(M+1):
        x = xi(i,a,b,M) ; px += [x]
        y = f(x)        ; py += [y]

    graph.plot(px, py)
    for i in range(N):
        px = []; py = []
        xs = xi(i, a, b, N);  ys = f(xs); px += [xs]; py += [ys]
        xe = xi(i+1, a, b, N);  ye = f(xe); px += [xe]; py += [ye]
        px = [xs] + px + [xe] + [xs]
        py = [ 0] + py + [ 0] + [ 0]
        graph.plot(px , py)

    plot.show()

N = 8
a = 0
b = pi

draw(a, b,N)

input("[Enter]キーを押して終了")
