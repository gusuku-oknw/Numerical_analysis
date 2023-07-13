"""
学籍：1213033903
氏名：玉城洵弥
内容：ルンゲ-ルッタ法
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


def rk4(T, N, Y1, Y2):
    dt = T / N
    x = [0] * (N + 1)
    y1 = [0] * (N + 1)
    y1[0] = Y1
    y2 = [0] * (N + 1)
    y2[0] = Y2

    for j in range(N + 1):
        t = j * dt; x[j] = t # 時刻
        k11 = f1(t, Y1, Y2)
        k21 = f2(t, Y1, Y2)
        k12 = f1(t + dt / 2, Y1 + dt / 2 * k11, Y2 + dt / 2 * k21)
        k22 = f2(t + dt / 2, Y1 + dt / 2 * k11, Y2 + dt / 2 * k21)
        k13 = f1(t + dt / 2, Y1 + dt / 2 * k12, Y2 + dt / 2 * k22)
        k23 = f2(t + dt / 2, Y1 + dt / 2 * k12, Y2 + dt / 2 * k22)
        k14 = f1(t + dt, Y1 + dt * k13, Y2 + dt * k23)
        k24 = f2(t + dt, Y1 + dt * k13, Y2 + dt * k23)
        Y1 += dt / 6 * (k11 + 2 * k12 + 2 * k13 + k14)
        y1[j] = Y1
        Y2 += dt / 6 * (k21 + 2 * k22 + 2 * k23 + k24)
        y2[j] = Y2

    x[N] = N * dt # 最後の時刻

    return x, y1, y2


T = 1
N1 = 10; N2 = 5
Y1 = 1; Y2 = 0

x, y1, y2 = rk4(T, N1, Y1, Y2)
a, b1, b2 = rk4(T, N2, Y1, Y2)
draw(x, y1, a, b1)
