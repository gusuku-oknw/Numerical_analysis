import matplotlib
import matplotlib.pyplot as plot


# 描画
def draw(x, y):
    fig = plot.figure()
    axe1 = fig.add_subplot(2, 1, 1)
    axe2 = fig.add_subplot(2, 1, 2)
    axe1.plot(x, y)
    axe2.plot(x, color="red", marker="o")
    axe2.plot(y, color="blue", marker="o")
    plot.show()


x = [0, 1, 2, 3]
y = [3, 2, 1, 0]
draw(x, y)
