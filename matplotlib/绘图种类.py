# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D


def scatter():
    n = 1024  # data size
    X = np.random.normal(0, 1, n)  # 每一个点的X值
    Y = np.random.normal(0, 1, n)  # 每一个点的Y值
    T = np.arctan2(Y, X)  # for color value
    plt.scatter(X, Y, s=75, c=T, alpha=.5)

    plt.xlim(-1.5, 1.5)
    plt.xticks(())  # ignore xticks
    plt.ylim(-1.5, 1.5)
    plt.yticks(())  # ignore yticks

    plt.show()


def bar():
    n = 12
    X = np.arange(n)
    Y1 = (1 - X / float(n)) * np.random.uniform(0.5, 1.0, n)
    Y2 = (1 - X / float(n)) * np.random.uniform(0.5, 1.0, n)

    plt.bar(X, +Y1, facecolor='#9999ff', edgecolor='white')
    plt.bar(X, -Y2, facecolor='#ff9999', edgecolor='white')

    plt.xlim(-.5, n)
    plt.xticks(())
    plt.ylim(-1.25, 1.25)
    plt.yticks(())
    for x, y in zip(X, Y1):
        # ha: horizontal alignment
        # va: vertical alignment
        plt.text(x + 0.4, y + 0.05, '%.2f' % y, ha='center', va='bottom')

    for x, y in zip(X, Y2):
        # ha: horizontal alignment
        # va: vertical alignment
        plt.text(x + 0.4, -y - 0.05, '%.2f' % y, ha='center', va='top')
    plt.show()


def f(x, y):
    # the height function
    return (1 - x / 2 + x ** 5 + y ** 3) * np.exp(-x ** 2 - y ** 2)


def contours():
    n = 256
    x = np.linspace(-3, 3, n)
    y = np.linspace(-3, 3, n)
    X, Y = np.meshgrid(x, y)
    # use plt.contourf to filling contours
    # X, Y and value for (X,Y) point
    plt.contourf(X, Y, f(X, Y), 8, alpha=.75, cmap=plt.cm.hot)
    C = plt.contour(X, Y, f(X, Y), 8, colors='black', linewidth=.5)
    plt.clabel(C, inline=True, fontsize=10)
    plt.xticks(())
    plt.yticks(())
    plt.show()


def images():
    a = np.array([0.313660827978, 0.365348418405, 0.423733120134,
                  0.365348418405, 0.439599930621, 0.525083754405,
                  0.423733120134, 0.525083754405, 0.651536351379]).reshape(3, 3)
    plt.imshow(a, interpolation='nearest', cmap='bone', origin='lower')
    plt.colorbar(shrink=.92)

    plt.xticks(())
    plt.yticks(())
    plt.show()


def data_3d():
    fig = plt.figure()
    # ax = Axes3D(fig)
    ax = Axes3D(fig, auto_add_to_figure=False)
    fig.add_axes(ax)
    # ax = fig.add_subplot(111, projection='3d')
    # X, Y value
    X = np.arange(-4, 4, 0.25)
    Y = np.arange(-4, 4, 0.25)
    X, Y = np.meshgrid(X, Y)  # x-y 平面的网格
    R = np.sqrt(X ** 2 + Y ** 2)
    # height value
    Z = np.sin(R)
    ax.plot_surface(X, Y, Z, rstride=1, cstride=1, cmap=plt.get_cmap('rainbow'))
    ax.contourf(X, Y, Z, zdir='z', offset=-2, cmap=plt.get_cmap('rainbow'))
    ax.set_zlim(-2, 2)
    plt.show()


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press ⌘F8 to toggle the breakpoint.
    # 散点图 Scatter
    # scatter()
    # 柱状条形图
    # bar()
    # 等高线图 Contours
    # contours()
    # 图片 Image
    # images()
    # 3D 图像
    data_3d()


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('绘图种类')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
