import draw


def progress(k, x):
    axe = []
    print(k, end="")
    for val in x:
        # print(' {:.8f}'.format(val), end="")
        axe.append(val)
    print(axe)
    return axe


def sor(N, A, b, omega, M):
    x = [0] * N
    axe = [progress(0, x)]

    for k in range(1, M + 1):
        for i in range(N):
            total = 0
            for j in range(N):
                if i != j:
                    total += A[i][j] * x[j]
            x[i] = omega * (b[i] - total) / A[i][i] + 1 - omega * x[i]
        axe.append(progress(k, x))

    return x, axe


N = 2
A = [[5, 4], [2, 3]]
b = [13, 8]
omega = 1.2
M = 21

axe_t = []

x, axe = sor(N, A, b, omega, M)


for i in range(len(axe[0])):
    tmp = []
    for v in axe:
        tmp.append(v[i])
    axe_t.append(tmp)
print(axe_t)
draw.draw(axe_t[0], axe_t[1])

input("[Enter]キーを押してください")
