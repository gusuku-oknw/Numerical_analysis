"""
学籍：1213033903
氏名：玉城洵弥
内容：オイラー
"""

import matplotlib
import matplotlib.pyplot as plt
from math import *


def draw(x, y, a, b):
    fig = plt.figure()
    graph = fig.add_subplot()
    graph.plot(x, y)
    graph.plot(a, b)
    graph.scatter(x, y, s=30)

    plt.show()


def f1(t, Y1, Y2):
    return Y2


def f2(t, Y1, Y2):
    return -16 * Y1 - 10 * Y2


def euler(T, N, Y1, Y2):
    dt = T / N; x = [0] * (N + 1)

    y1 = [0] * (N + 1)
    y2 = [0] * (N + 1)

    y1[0] = Y1
    y2[0] = Y2

    for j in range(N):
        t = j * dt; x[j] = t # 時刻
        Y1 += dt * f1(t, Y1, Y2); Y2 += dt * f2(t, Y1, Y2) # 次の時刻の位置
        y1[j + 1] = Y1; y2[j + 1] = Y2

    x[N] = N * dt # 最後の時刻
    return x, y1, y2


T = 1
N1 = 10; N2 = 5
Y1 = 1; Y2 = 0

# オイラー法
x, y1, y2 = euler(T, N1, Y1, Y2)
a, b1, b2 = euler(T, N2, Y1, Y2)
draw(x, y1, a, b1)
# print("{0:5d} {1:6.4f} {2:8.6f}".format(N, T/N, y[N]))
