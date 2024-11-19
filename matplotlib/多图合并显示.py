# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec
import numpy as np


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press ⌘F8 to toggle the breakpoint.


def subplot01():
    plt.figure()
    plt.subplot(2, 2, 1)
    plt.plot([0, 1], [0, 1])
    plt.subplot(2, 2, 2)
    plt.plot([0, 1], [0, 2])
    plt.subplot(223)
    plt.plot([0, 1], [0, 3])
    plt.subplot(224)
    plt.plot([0, 1], [0, 4])
    plt.show()


def subplot02():
    plt.subplot(2, 1, 1)
    plt.plot([0, 1], [0, 1])
    plt.subplot(2, 3, 4)
    plt.plot([0, 1], [0, 2])
    plt.subplot(235)
    plt.plot([0, 1], [0, 3])

    plt.subplot(236)
    plt.plot([0, 1], [0, 4])
    plt.show()


def subplot_grid_01():
    plt.figure()
    ax1 = plt.subplot2grid((3, 3), (0, 0), colspan=3)
    ax1.plot([1, 2], [1, 2])  # 画小图
    ax1.set_title('ax1_title')  # 设置小图的标题
    ax2 = plt.subplot2grid((3, 3), (1, 0), colspan=2)
    ax3 = plt.subplot2grid((3, 3), (1, 2), rowspan=2)
    ax4 = plt.subplot2grid((3, 3), (2, 0))
    ax5 = plt.subplot2grid((3, 3), (2, 1))
    ax4.scatter([1, 2], [2, 2])
    ax4.set_xlabel('ax4_x')
    ax4.set_ylabel('ax4_y')
    plt.show()


def subplot_grid_spec():
    plt.figure()
    gs = gridspec.GridSpec(3, 3)
    ax6 = plt.subplot(gs[0, :])
    ax7 = plt.subplot(gs[1, :2])
    ax8 = plt.subplot(gs[1:, 2])
    ax9 = plt.subplot(gs[-1, 0])
    ax10 = plt.subplot(gs[-1, -2])
    plt.show()


def subplot_s():
    f, ((ax11, ax12), (ax13, ax14)) = plt.subplots(2, 2, sharex=True, sharey=True)
    ax11.scatter([1, 2], [1, 2])
    plt.tight_layout()
    plt.show()


def plot_in_plot():
    # 初始化figure
    fig = plt.figure()

    # 创建数据
    x = [1, 2, 3, 4, 5, 6, 7]
    y = [1, 3, 4, 2, 5, 8, 6]
    left, bottom, width, height = 0.1, 0.1, 0.8, 0.8
    ax1 = fig.add_axes([left, bottom, width, height])
    ax1.plot(x, y, 'r')
    ax1.set_xlabel('x')
    ax1.set_ylabel('y')
    ax1.set_title('title')
    # 左上角
    left, bottom, width, height = 0.2, 0.6, 0.25, 0.25
    ax2 = fig.add_axes([left, bottom, width, height])
    ax2.plot(y, x, 'b')
    ax2.set_xlabel('x')
    ax2.set_ylabel('y')
    ax2.set_title('title inside 1')
    # 右下角
    plt.axes([0.6, 0.2, 0.25, 0.25])
    plt.plot(y[::-1], x, 'g')  # 注意对y进行了逆序处理
    plt.xlabel('x')
    plt.ylabel('y')
    plt.title('title inside 2')

    plt.show()


def twinx():
    x = np.arange(0, 10, 0.1)
    y1 = 0.05 * x ** 2
    y2 = -1 * y1
    _, ax1 = plt.subplots()
    ax2 = ax1.twinx()
    ax1.plot(x, y1, 'g-')  # green, solid line
    ax1.set_xlabel('X data')
    ax1.set_ylabel('Y1 data', color='g')
    ax2.plot(x, y2, 'b-')  # blue
    ax2.set_ylabel('Y2 data', color='b')
    plt.show()


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('多图合并显示')
    # Subplot 多合一显示，均匀图中图
    # subplot01()
    # Subplot 多合一显示，不均匀图中图
    # subplot02()

    # Subplot 分格显示
    # subplot_grid_01()
    # subplot_grid_spec()
    # subplot_s()

    # 图中图 plot in plot
    # plot_in_plot()

    # 次坐标轴 twinx
    twinx()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
