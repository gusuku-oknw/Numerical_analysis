"""
学籍：1213033903
氏名：玉城洵弥
"""
import numpy as np
import matplotlib
import matplotlib.pyplot as plot


# gauss
def gauss(N, A, y):
    x = [0] * N

    for k in range(N - 1):
        m = 0
        for i in range(k, N):
            if m < abs(A[i][k]):
                m = abs(A[i][k])
                l = i
            if l != k:
                for n in range(k, N):
                    A[k][n], A[l][n] = A[l][n], A[k][n]
                y[k], y[l] = y[l], y[k]
        for i in range(k + 1, N):
            alpha = A[i][k] / A[k][k]
            for j in range(k + 1, N):
                A[i][j] -= alpha * A[k][j]
            y[i] -= alpha * y[k]
    x[N - 1] = y[N - 1] / A[N - 1][N - 1]

    for i in range(N - 2, -1, -1):
        s = 0
        for k in range(i + 1, N):
            s += A[i][k] * x[k]
        x[i] = (y[i] - s) / A[i][i]

    return x


def f1(x):
    return x * x


def f2(x):
    return x


def f3(x):
    return 1


# 描画
def draw(x, y, a, b):
    fig = plot.figure()
    graph = fig.add_subplot()
    graph.plot([0, x.max()], [b, a * x.max() + b])
    graph.scatter(x, y, s=30, c="red")
    plot.show()


def leastsquares(N, x, y):
    # p11 = 0.0;
    # p12 = 0.0;
    # p13 = 0.0
    # p21 = 0.0;
    # p22 = 0.0;
    # p23 = 0.0
    # p31 = 0.0;
    # p32 = 0.0;
    # p33 = 0.0
    #
    # for j in range(N):
    #     xj = x[j]
    #     p11 += f1(xj) * f1(xj);
    #     p12 += f1(xj) * f2(xj);
    #     p13 += f1(xj) * f3(xj)
    #     p21 += f2(xj) * f1(xj);
    #     p22 += f2(xj) * f2(xj);
    #     p23 += f2(xj) * f3(xj)
    #     p31 += f3(xj) * f1(xj);
    #     p32 += f3(xj) * f2(xj);
    #     p33 += f3(xj) * f3(xj)
    # pki = [[p11, p12, p13],
    #        [p21, p22, p23],
    #        [p31, p32, p33]
    #        ]
    # q1 = 0.0;
    # q2 = 0.0;
    # q3 = 0.0
    # for j in range(N):
    #     xj = x[j];
    #     yj = y[j]
    #     q1 += yj * f1(xj);
    #     q2 += yj * f2(xj);
    #     q3 += yj * f3(xj)
    # qk = [q1, q2, q3]
    #
    # return gauss(3, pki, qk)
    a = ((np.dot(x, y) - y.sum() * x.sum() / N) /
         ((x ** 2).sum() - x.sum() ** 2 / N))
    b = (y.sum() - a * x.sum())/N

    return a, b


N = 5
x = np.array([0.0, 0.5, 1.0, 1.5, 2.0])
y = np.array([-0.45, 0.20, 0.53, 0.28, -0.62])
a, b = leastsquares(N, x, y)
# print("A={}, B={}, C=[]".format(ABC[0], ABC[1], ABC[2]))
M = 20
draw(x, y, a, b)

input("[Enter]キーを押して終了")
