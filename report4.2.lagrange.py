"""
学籍：1213033903
氏名：玉城洵弥
"""
import numpy as np
import matplotlib
import matplotlib.pyplot as plot


# Gaussの消去法
def gauss(N, A, b):
    x = [0] * N
    x_new = [0] * N
    error = 0
    eps = 1.0e-4
    sum = 0
    for _ in range(1, N + 1):
        for i in range(N):
            total = 0
            for j in range(N):
                if i != j:
                    total += A[i][j] * x[j]
            x_new[i] = (b[i] - total) / A[i][i]

        for i in range(N):
            x[i] = x_new[i]
    return x


def xi(i, xs, xe, ndiv):
    return xs * (ndiv - i) / ndiv + xe * i / ndiv


# 描画
def draw(px, py, lx, ly):
    fig = plot.figure()
    graph = fig.add_subplot()
    graph.set_xlim(px[0], px[-1])

    graph.plot(lx, ly)

    graph.scatter(px, py, s=30, c="red")
    plot.show()


def lagrange(px, py, x):
    N = len(px)
    y = 0.0

    for j in range(N):
        lj = 1.0
        for i in range(N):
            if i != j:
                lj = lj * (x - px[i]) / (px[j] - px[i])
        y += py[j] * lj
    return y


def f(x):
    return 1 / (1 + 25 * x ** 2)


N = 9
px = np.array([-1, -0.75, -0.5, -0.25, 0, 0.25, 0.5, 0.75, 1])
py = np.array([0,    0.5,    1,   0.5, 0, -0.5,  -1, -0.5, 0])

# サンプルデータの作成

M = 200
xs = -1.0
xe = 1.0

lx = np.array([])
ly = np.array([])

for i in range(M + 1):
    x = xi(i, -1.0, 1.0, M)
    y = lagrange(px, py, x)
    lx = np.append(lx, x)
    ly = np.append(ly, y)


draw(px, py, lx, ly)

input("[Enter]キーを押して終了")
