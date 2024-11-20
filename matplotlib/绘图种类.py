# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D


def scatter():
    # 数据大小
    n = 1024
    # 生成 n 个X值，符合标准正态分布
    X = np.random.normal(0, 1, n)
    # 生成 n 个Y值，符合标准正态分布
    Y = np.random.normal(0, 1, n)
    # 根据Y和X的值计算颜色值
    T = np.arctan2(Y, X)

    # 绘制散点图，大小为75，颜色为T，透明度为0.5
    plt.scatter(X, Y, s=75, c=T, alpha=.5)

    # 设置x轴的显示范围
    plt.xlim(-1.5, 1.5)
    # 不显示x轴刻度
    plt.xticks(())
    # 设置y轴的显示范围
    plt.ylim(-1.5, 1.5)
    # 不显示y轴刻度
    plt.yticks(())

    # 显示图形
    plt.show()


def bar():
    n = 12  # 柱状图中的柱子数量
    X = np.arange(n)  # X轴上的位置
    print(X)
    # 生成 Y1 的值，这些值随 X 增大而减小，范围在0.5到1.0之间随机
    Y1 = (1 - X / float(n)) * np.random.uniform(0.5, 1.0, n)
    # 生成 Y2 的值，同样是随 X 增大而减小，范围在0.5到1.0之间随机
    Y2 = (1 - X / float(n)) * np.random.uniform(0.5, 1.0, n)

    # 绘制 Y1 的正向柱状图，设置面颜色和边缘颜色
    plt.bar(X, +Y1, facecolor='#9999ff', edgecolor='white')
    # 绘制 Y2 的反向柱状图，设置面颜色和边缘颜色
    plt.bar(X, -Y2, facecolor='#ff9999', edgecolor='white')

    # 设置X轴的显示范围
    plt.xlim(-.5, n)
    # 不显示X轴刻度
    plt.xticks(())
    # 设置Y轴的显示范围
    plt.ylim(-1.25, 1.25)
    # 不显示Y轴刻度
    plt.yticks(())
    # 在每个柱状图上方添加数值标签
    for x, y in zip(X, Y1):
        # 在柱状图上方显示Y值，ha和va分别控制水平和垂直对齐方式
        plt.text(x + 0.1, y + 0.05, '%.2f' % y, ha='center', va='bottom')

    # 在每个柱状图下方添加数值标签
    for x, y in zip(X, Y2):
        # 在柱状图下方显示Y值，ha和va分别控制水平和垂直对齐方式
        plt.text(x + 0.1, -y - 0.05, '%.2f' % y, ha='center', va='top')
    # 显示图表
    plt.show()


def f(x, y):
    # 定义一个高度函数，该函数基于给定的x和y坐标计算一个高度值
    return (1 - x / 2 + x ** 5 + y ** 3) * np.exp(-x ** 2 - y ** 2)


def contours():
    n = 256  # 设置网格点的数量
    x = np.linspace(-3, 3, n)  # 在-3到3之间生成n个x坐标点
    y = np.linspace(-3, 3, n)  # 在-3到3之间生成n个y坐标点
    X, Y = np.meshgrid(x, y)  # 生成网格点坐标的矩阵

    # 使用plt.contourf创建填充的等高线图
    # X, Y为网格点坐标，f(X, Y)计算每个点对应的高度值
    plt.contourf(X, Y, f(X, Y), 8, alpha=.75, cmap=plt.cm.hot)

    # 创建等高线，设置等高线数量为8，颜色为黑色，线宽为0.5
    C = plt.contour(X, Y, f(X, Y), 8, colors='black', linewidths=.5)
    # 在等高线上标注高度值，设置字体大小为10
    plt.clabel(C, inline=True, fontsize=10)
    # 不显示x轴刻度
    plt.xticks(())
    # 不显示y轴刻度
    plt.yticks(())
    # 显示图形
    plt.show()


def images():
    # 创建一个 3x3 的矩阵，用于表示图像数据
    a = np.array([
        0.313660827978, 0.365348418405, 0.423733120134,
        0.365348418405, 0.439599930621, 0.525083754405,
        0.423733120134, 0.525083754405, 0.651536351379
    ]).reshape(3, 3)

    # 使用plt.imshow显示这个矩阵，颜色映射使用'bone'，并设置原点为图像的左下角
    plt.imshow(a, interpolation='nearest', cmap='bone', origin='lower')
    # 添加颜色条，并设置压缩比例为0.92以更好地适配显示
    plt.colorbar(shrink=.92)

    # 不显示x轴刻度
    plt.xticks(())
    # 不显示y轴刻度
    plt.yticks(())
    # 显示图形
    plt.show()


def data_3d():
    # 创建一个新的图形
    fig = plt.figure()
    # 创建一个3D坐标系，不自动添加到图形中（处理了更新的matplotlib用法）
    ax = Axes3D(fig, auto_add_to_figure=False)
    # 手动将坐标系添加到图形中
    fig.add_axes(ax)

    # 生成X和Y数据，范围从-4到4，步长为0.25
    X = np.arange(-4, 4, 0.25)
    Y = np.arange(-4, 4, 0.25)
    # 生成网格数据，用于3D图形的基础
    X, Y = np.meshgrid(X, Y)
    # 计算R，作为X和Y的函数，用于生成高度数据Z
    R = np.sqrt(X ** 2 + Y ** 2)
    # 计算Z值，使用正弦函数模拟高度变化
    Z = np.sin(R)

    # 绘制3D表面图，设置行和列的步长，颜色映射使用彩虹色
    ax.plot_surface(X, Y, Z, rstride=1, cstride=1, cmap=plt.get_cmap('rainbow'))
    # 绘制Z方向的等高线图，将等高线设置在Z=-2的位置，使用彩虹色
    ax.contourf(X, Y, Z, zdir='z', offset=-2, cmap=plt.get_cmap('rainbow'))
    # 设置Z轴的显示范围
    ax.set_zlim(-2, 2)
    # 显示图形
    plt.show()


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press ⌘F8 to toggle the breakpoint.
    # 散点图 Scatter
    scatter()
    # 柱状条形图
    bar()
    # 等高线图 Contours
    contours()
    # 图片 Image
    images()
    # 3D 图像
    data_3d()


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('绘图种类')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
