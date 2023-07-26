"""
学籍：1213033903
氏名：玉城洵弥
内容：wave equation
"""
import matplotlib.pyplot as plt


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


def Phi(x):
    return 2 * x * (1 - x)


N = 6
M = 100
T = 1
draw = [0, 4, 8, 12, 16, 20]

dx = 1 / N
dt = 1 / M
a = dt / (dx * dx)

x = [0] * (N + 1)
for j in range(N + 1):
    x[j] = Phi(j * dx)

cur_U = [0] * (N + 1)
cur_U[0] = 0
cur_U[N] = 0
old_U = [0] * (N + 1)
old_U[0] = 0
old_U[N] = 0

new_U = [0] * (N + 1)
for j in range(N + 1):
    new_U[j] = Phi(j * dx)

fig = plt.figure()
graph = fig.add_subplot()
graph.set_xlim([0, 1])
graph.set_ylim([0, 1])
graph.set_aspect("equal")

for n in range(M):
    A = []
    for i in range(N - 1):
        A += [[0] * (N - 1)]
    for i in range(N - 1):
        A[i][i] = 1 + 2 * a
    for i in range(N - 2):
        A[i][i + 1] = -a
        A[i + 1][i] = -a

    y = [0] * (N - 1)
    for i in range(N - 1):
        # 変更
        y[i] = 2*cur_U[i+1] - old_U[i+1]
    new_U = [0] + gauss(N - 1, A, y) + [0]

    if n in draw:
        graph.plot(x, new_U)
        graph.scatter(x, new_U, s=30)

    old_U = cur_U
    cur_U = new_U

plt.show()
