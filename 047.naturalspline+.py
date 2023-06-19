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


def f1(x):
    return x * x


# 描画
def draw(xmin, xmax, px, py, a, b, c, d):
    fig = plot.figure()
    graph = fig.add_subplot()
    graph.set_xlim(xmin, xmax)
    #
    dx = (xmax - xmin) / len(a)
    for j in range(len(a)):
        xj = px[j]
        # xk = px[j+1] 必要ない?
        qx = []
        qy = []
        M = 10
        for i in range(M + 1):
            x = xj + dx * i / M
            qx += [x]
            qy += [a[j] * (x - xj) * (x - xj) * (x - xj) + b[j] * (x - xj) * (x - xj) + c[j] * (x - xj) + d[j]]
        graph.plot(qx, qy)
        graph.scatter(px, py, s=30, c='red')
    plot.show()


def naturalspline(N, px, py):
    h = [0] * N
    for j in range(N):
        h[j] = px[j + 1] - px[j]
    v = [0] * N
    for j in range(N):
        v[j] = 6 * ((py[j + 1] - py[j]) / h[j] - (py[j] - py[j - 1]) / h[j - 1])
    #
    A = []
    for i in range(N - 1):
        A += [[0] * (N - 1)]

    for i in range(N - 1):
        A[i][i] = 2 * (h[i] + h[i + 1])  # 対角成分
    for i in range(N - 2):
        A[i][i + 1] = h[i + 1]  # 対角周辺
        A[i + 1][i] = h[i]  # 対角周辺
    y = [0] * (N - 1)  # 右辺ベクトル
    for i in range(N - 1):
        y[i] = v[i + 1]

    x = gauss(N - 1, A, y)

    u = [0] + x + [0]

    b = [0] * N
    for j in range(N):
        b[j] = u[j] / 2
    a = [0] * N
    for j in range(N):
        a[j] = (u[j + 1] - u[j]) / (6 * (px[j + 1] - px[j]))
    d = [0] * N
    for j in range(N):
        d[j] = py[j]
    c = [0] * N
    for j in range(N):
        c[j] = (py[j + 1] - py[j]) / (px[j + 1] - px[j]) - (px[j + 1] - px[j]) * (2 * u[j] + u[j + 1]) / 6

    return a, b, c, d


def f(x):
    return np.sin(x) / (1 + x)


N = 10
px = np.array([])
py = np.array([])
for i in range(0, N + 1):
    x = 3 * np.pi * i / N
    px = np.append(px, x)
    py = np.append(py, f(x))

# a, b = leastsquares(N, x, y)
# print("A={}, B={}, C=[]".format(ABC[0], ABC[1], ABC[2]))
M = 20

a, b, c, d = naturalspline(N, px, py)
draw(0, 3 * np.pi, px, py, a, b, c, d)

input("[Enter]キーを押して終了")
