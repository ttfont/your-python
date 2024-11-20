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
    # 创建一个图形窗口
    plt.figure()
    # 在2x2的网格中创建第1个子图位置
    plt.subplot(2, 2, 1)
    # 在第1个子图中绘制一条线，从(0,0)到(1,1)
    plt.plot([0, 1], [0, 1])

    # 在2x2的网格中创建第2个子图位置
    plt.subplot(2, 2, 2)
    # 在第2个子图中绘制一条线，从(0,0)到(1,2)
    plt.plot([0, 1], [0, 2])

    # 在2x2的网格中创建第3个子图位置，使用另一种指定方式223
    plt.subplot(223)
    # 在第3个子图中绘制一条线，从(0,0)到(1,3)
    plt.plot([0, 1], [0, 3])

    # 在2x2的网格中创建第4个子图位置，使用另一种指定方式224
    plt.subplot(224)
    # 在第4个子图中绘制一条线，从(0,0)到(1,4)
    plt.plot([0, 1], [0, 4])

    # 显示图形窗口
    plt.show()


def subplot02():
    # 在2行1列的网格中创建第1个子图位置，此子图占据第一行的全部
    plt.subplot(2, 1, 1)
    # 在第1个子图中绘制一条线，从(0,0)到(1,1)
    plt.plot([0, 1], [0, 1])

    # 在2行3列的网格中创建第4个子图位置，这里的子图位于第二行的第一个位置
    plt.subplot(2, 3, 4)
    # 在第2个子图中绘制一条线，从(0,0)到(1,2)
    plt.plot([0, 1], [0, 2])

    # 使用简写方式235，等同于在2行3列的网格中指定第5个子图，即第二行的第二个位置
    plt.subplot(235)
    # 在第3个子图中绘制一条线，从(0,0)到(1,3)
    plt.plot([0, 1], [0, 3])

    # 使用简写方式236，等同于在2行3列的网格中指定第6个子图，即第二行的第三个位置
    plt.subplot(236)
    # 在第4个子图中绘制一条线，从(0,0)到(1,4)
    plt.plot([0, 1], [0, 4])

    # 显示图形窗口
    plt.show()


def subplot_grid_01():
    # 创建一个新的图形窗口
    plt.figure()
    # 创建一个子图，占据3行3列网格的第0行所有3列
    ax1 = plt.subplot2grid((3, 3), (0, 0), colspan=3)
    ax1.plot([1, 2], [1, 2])  # 在ax1中绘制线图
    ax1.set_title('ax1_title')  # 设置ax1的标题

    # 创建一个子图，占据第1行的前2列
    ax2 = plt.subplot2grid((3, 3), (1, 0), colspan=2)
    # 创建一个子图，从第1行第3列开始，纵向跨越2行
    ax3 = plt.subplot2grid((3, 3), (1, 2), rowspan=2)
    # 创建一个子图，在第2行第1列
    ax4 = plt.subplot2grid((3, 3), (2, 0))
    # 创建一个子图，在第2行第2列
    ax5 = plt.subplot2grid((3, 3), (2, 1))

    # 在ax4中绘制散点图
    ax4.scatter([1, 2], [2, 2])
    # 设置ax4的x轴标签
    ax4.set_xlabel('ax4_x')
    # 设置ax4的y轴标签
    ax4.set_ylabel('ax4_y')

    # 显示图形窗口
    plt.show()


def subplot_grid_spec():
    # 创建一个图形窗口
    plt.figure()
    # 初始化一个网格布局，3行3列
    gs = gridspec.GridSpec(3, 3)

    # 创建一个子图，占据第一行的所有3列
    plt.subplot(gs[0, :])
    # 创建一个子图，占据第二行的前两列
    plt.subplot(gs[1, :2])
    # 创建一个子图，占据第二行的第三列，并延伸至第三行
    plt.subplot(gs[1:, 2])
    # 创建一个子图，位于最后一行的第一列
    plt.subplot(gs[-1, 0])
    # 创建一个子图，位于最后一行的第二列
    plt.subplot(gs[-1, -2])

    # 显示图形
    plt.show()


def subplot_s():
    # 创建一个2行2列的子图网格，并共享x轴和y轴
    # 返回的f是整个图形对象，((ax11, ax12), (ax13, ax14))是子图的坐标轴对象
    f, ((ax11, ax12), (ax13, ax14)) = plt.subplots(2, 2, sharex=True, sharey=True)

    # 在第一个子图(ax11)中绘制散点图
    ax11.scatter([1, 2], [1, 2])

    # 调整子图之间的间距，以防止重叠
    plt.tight_layout()

    # 显示图形
    plt.show()


def plot_in_plot():
    # 初始化figure对象
    fig = plt.figure()

    # 创建基础数据
    x = [1, 2, 3, 4, 5, 6, 7]
    y = [1, 3, 4, 2, 5, 8, 6]

    # 设置大图的坐标轴位置
    left, bottom, width, height = 0.1, 0.1, 0.8, 0.8
    ax1 = fig.add_axes([left, bottom, width, height])  # 添加大图
    ax1.plot(x, y, 'r')  # 大图中绘制红色线条
    ax1.set_xlabel('x')  # 设置x轴标签
    ax1.set_ylabel('y')  # 设置y轴标签
    ax1.set_title('title')  # 设置大图标题

    # 在大图中嵌入小图1：左上角
    left, bottom, width, height = 0.2, 0.6, 0.25, 0.25
    ax2 = fig.add_axes([left, bottom, width, height])  # 添加小图1
    ax2.plot(y, x, 'b')  # 小图1中绘制蓝色线条
    ax2.set_xlabel('x')  # 设置小图1的x轴标签
    ax2.set_ylabel('y')  # 设置小图1的y轴标签
    ax2.set_title('title inside 1')  # 设置小图1标题

    # 在大图中嵌入小图2：右下角
    plt.axes([0.6, 0.2, 0.25, 0.25])  # 添加小图2
    plt.plot(y[::-1], x, 'g')  # 小图2中绘制绿色线条，y数据逆序处理
    plt.xlabel('x')  # 设置小图2的x轴标签
    plt.ylabel('y')  # 设置小图2的y轴标签
    plt.title('title inside 2')  # 设置小图2标题

    # 显示最终图形
    plt.show()


def twinx():
    # 创建x轴的数据，从0到10，步长0.1
    x = np.arange(0, 10, 0.1)
    # 创建y1数据，y1是x的平方乘以0.05
    y1 = 0.05 * x ** 2
    # 创建y2数据，y2是y1的相反数
    y2 = -1 * y1

    # 创建一个图和一个子图轴ax1
    _, ax1 = plt.subplots()
    # 创建第二个y轴ax2，共享ax1的x轴
    ax2 = ax1.twinx()

    # 在ax1上绘制x和y1的关系，线条为绿色实线
    ax1.plot(x, y1, 'g-')  # green, solid line
    # 设置ax1的x轴和y轴标签
    ax1.set_xlabel('X data')
    ax1.set_ylabel('Y1 data', color='g')

    # 在ax2上绘制x和y2的关系，线条为蓝色实线
    ax2.plot(x, y2, 'b-')  # blue
    # 设置ax2的y轴标签，并设置文字颜色为蓝色
    ax2.set_ylabel('Y2 data', color='b')

    # 显示图表
    plt.show()


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('多图合并显示')
    # Subplot 多合一显示，均匀图中图
    subplot01()
    # Subplot 多合一显示，不均匀图中图
    subplot02()

    # Subplot 分格显示
    subplot_grid_01()
    subplot_grid_spec()
    subplot_s()

    # 图中图 plot in plot
    plot_in_plot()

    # 次坐标轴 twinx
    twinx()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
