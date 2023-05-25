import matplotlib
import matplotlib.pyplot as plot


# 描画
def draw(x, y):
    fig = plot.figure()
    plot.plot(x, color="red", marker="o")
    plot.plot(y, color="blue", marker="o")
    # plot.scatter(x, y, s=30, c="red")
    # plot.scatter(y, x, s=30, c="blue")
    plot.show()

x = [0, 1, 2, 3]
y = [3, 2, 1, 0]
draw(x, y)