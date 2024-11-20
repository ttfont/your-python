import matplotlib
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.font_manager import FontManager


# 基本用法
def figure1():
    # 生成50个等间距的点，范围从-1到1
    x = np.linspace(-1, 1, 50)

    # 定义函数 y = 2x + 1
    y = 2 * x + 1

    # 创建一个图形窗口
    plt.figure()

    # 绘制 x 和 y 的关系
    plt.plot(x, y)

    # 显示图形
    plt.show()


# figure 图像
def figure2():
    # 生成50个等间距的点，范围从-3到3
    x = np.linspace(-3, 3, 50)

    # 定义第一个函数 y1 = 2x + 1
    y1 = 2 * x + 1

    # 定义第二个函数 y2 = x^2
    y2 = x ** 2

    # 创建一个图形窗口
    plt.figure()

    # 绘制 x 和 y1 的关系（线性）
    plt.plot(x, y1)

    # 绘制 x 和 y2 的关系（二次方）
    plt.plot(x, y2)

    # 显示图形
    plt.show()


# figure 图像
def figure3():
    # 使用 numpy 的 linspace 函数生成一个从 -3 到 3 的等差数列，包含 50 个元素
    x = np.linspace(-3, 3, 50)
    # 定义函数 y1 为线性函数 2x + 1
    y1 = 2 * x + 1
    # 定义函数 y2 为二次函数 x^2
    y2 = x ** 2

    # 创建一个编号为 3 的图形窗口，设置窗口大小为 8x4 英寸
    plt.figure(num=3, figsize=(8, 4))
    # 在图形窗口中绘制 y2 = x^2 的图形
    plt.plot(x, y2)
    # 在同一个图形窗口中绘制 y1 = 2x + 1 的图形，设置图形颜色为红色，线宽为 1.0，线型为虚线
    plt.plot(x, y1, color='red', linewidth=1.0, linestyle='--')

    # 显示图形
    plt.show()


# 设置坐标轴1
def figure4():
    # 生成从 -3 到 3 的 50 个点的线性空间，赋值给变量 x
    x = np.linspace(-3, 3, 50)
    # 计算线性函数 y1 = 2x + 1
    y1 = 2 * x + 1
    # 计算二次函数 y2 = x^2
    y2 = x ** 2

    # 创建一个新的图形窗口
    plt.figure()
    # 在图形窗口中绘制 y2 = x^2 的图形
    plt.plot(x, y2)
    # 在同一个图形窗口中绘制 y1 = 2x + 1 的图形，设置图形颜色为红色，线宽为 1.0，线型为虚线
    plt.plot(x, y1, color='red', linewidth=1.0, linestyle='--')

    # 设置 x 轴的显示范围为 -1 到 2
    plt.xlim((-1, 2))
    # 设置 y 轴的显示范围为 -2 到 3
    plt.ylim((-2, 3))
    # 设置 x 轴的标签文本，即 x 轴的名称
    plt.xlabel('I am x')
    # 设置 y 轴的标签文本，即 y 轴的名称
    plt.ylabel('I am y')

    # 显示图形窗口
    plt.show()


# 设置坐标轴1
def figure5():
    # 生成 x 数据：从 -3 到 3 之间均匀分布的 50 个点
    x = np.linspace(-3, 3, 50)
    # 计算 y1 数据：y1 是 x 的线性函数
    y1 = 2 * x + 1
    # 计算 y2 数据：y2 是 x 的平方函数
    y2 = x ** 2

    # 创建一个新的绘图窗口
    plt.figure()
    # 绘制 y2 曲线
    plt.plot(x, y2)
    # 使用指定的参数绘制 y1 曲线，颜色为红色，线宽为 1.0，线型为虚线
    plt.plot(x, y1, color='red', linewidth=1.0, linestyle='--')
    # 设置 x 轴的显示范围为 -1 到 2
    plt.xlim((-1, 2))
    # 设置 y 轴的显示范围为 -2 到 3
    plt.ylim((-2, 3))
    # 设置 x 轴的标签为 "I am x"
    plt.xlabel('I am x')
    # 设置 y 轴的标签为 "I am y"
    plt.ylabel('I am y')

    # 创建新的刻度点，从 -1 到 2 之间均匀分布的 5 个点
    new_ticks = np.linspace(-1, 2, 5)
    # 打印新的刻度点
    print(new_ticks)
    # 设置 x 轴的刻度点
    plt.xticks(new_ticks)
    # 设置 y 轴的刻度点和对应的标签，标签用特殊的格式表示不同的意义
    plt.yticks([-2, -1.8, -1, 1.22, 3],
               [r'$really\ bad$', r'$bad$', r'$normal$', r'$good$', r'$really\ good$'])
    # 显示图形
    plt.show()


def figure6():
    # 生成从-3到3的50个线性等分点
    x = np.linspace(-3, 3, 50)
    # 计算 y1，根据线性方程 y = 2x + 1
    y1 = 2 * x + 1
    # 计算 y2，根据方程 y = x^2
    y2 = x ** 2

    # 创建图形
    plt.figure()
    # 绘制 x^2 曲线
    plt.plot(x, y2)
    # 绘制 2x + 1 曲线，设置为红色、线宽1.0、线型为虚线
    plt.plot(x, y1, color='red', linewidth=1.0, linestyle='--')

    # 设置 x 轴显示范围
    plt.xlim((-1, 2))
    # 设置 y 轴显示范围
    plt.ylim((-2, 3))

    # 创建新的 x 轴刻度点，从 -1 到 2 之间均匀分布的 5 个点
    new_ticks = np.linspace(-1, 2, 5)
    # 设置 x 轴刻度
    plt.xticks(new_ticks)
    # 设置 y 轴刻度和标签，标签为不同的质量等级
    plt.yticks([-2, -1.8, -1, 1.22, 3],
               ['$really\\ bad$', '$bad$', '$normal$', '$good$', '$really\\ good$'])

    # 获取当前坐标轴
    ax = plt.gca()
    # 设置右侧坐标轴颜色为无，使其不显示
    ax.spines['right'].set_color('none')
    # 设置顶部坐标轴颜色为无，使其不显示
    ax.spines['top'].set_color('none')

    # 设置 x 轴的刻度只在下方显示
    ax.xaxis.set_ticks_position('bottom')
    # 设置 x 轴的位置，使其通过数据点 y=0 的位置
    ax.spines['bottom'].set_position(('data', 0))

    # 设置 y 轴的刻度只在左侧显示
    ax.yaxis.set_ticks_position('left')
    # 设置 y 轴的位置，使其通过数据点 x=0 的位置
    ax.spines['left'].set_position(('data', 0))

    # 显示图形
    plt.show()


def figure7():
    # 生成从-3到3的50个线性等分点
    x = np.linspace(-3, 3, 50)
    # 定义第一条线的 y 值，依据线性方程 y = 2x + 1
    y1 = 2 * x + 1
    # 定义第二条线的 y 值，依据方程 y = x^2
    y2 = x ** 2

    # 创建图形
    plt.figure()
    # 设置 x 轴显示范围
    plt.xlim((-1, 2))
    # 设置 y 轴显示范围
    plt.ylim((-2, 3))

    # 创建新的 x 轴刻度点，从 -1 到 2 之间均匀分布的 5 个点
    new_sticks = np.linspace(-1, 2, 5)
    # 设置 x 轴刻度
    plt.xticks(new_sticks)
    # 设置 y 轴刻度和标签，标签为不同的质量等级
    plt.yticks([-2, -1.8, -1, 1.22, 3],
               [r'$really\ bad$', r'$bad$', r'$normal$', r'$good$', r'$really\ good$'])

    # 绘制线性线并指定图例标签
    l1, = plt.plot(x, y1, label='linear line')
    # 绘制二次方线，设置为红色、线宽1.0、线型为虚线，并指定图例标签
    l2, = plt.plot(x, y2, color='red', linewidth=1.0, linestyle='--', label='square line')
    # plt.legend(loc='upper right')
    # 添加图例，手动指定图例中各曲线的标签和位置
    plt.legend(handles=[l1, l2], labels=['up', 'down'], loc='best')

    # 显示图形
    plt.show()


def font_query():
    fm = FontManager()
    available_fonts = fm.ttflist

    for font in available_fonts:
        if 'Hei' in font.name or 'Song' in font.name:  # 查找包含“黑”或“宋”字的字体
            print(font.name, font.fname)


def figure8_1():
    # 设置matplotlib支持中文显示
    matplotlib.rcParams['font.family'] = 'Songti SC'  # 设置字体为黑体
    matplotlib.rcParams['font.size'] = 14  # 设置字体大小
    matplotlib.rcParams['axes.unicode_minus'] = False  # 正常显示负号
    # 使用 numpy 创建 x 范围从 -3 到 3 的线性空间，共 50 个点
    x = np.linspace(-3, 3, 50)
    # 定义函数 y = 2x + 1
    y = 2 * x + 1

    # 创建图形，编号为 1，大小为 8x5
    plt.figure(num=1, figsize=(8, 5))
    # 绘制 x 和 y 的图形
    plt.plot(x, y)
    # 获取当前轴域
    ax = plt.gca()
    # 设置图形的右边框和上边框为不显示
    ax.spines['right'].set_color('none')
    ax.spines['top'].set_color('none')
    # 设置 x 轴的刻度位置在底部
    ax.xaxis.set_ticks_position('bottom')
    # 设置底部边框位置在 y=0 的位置
    ax.spines['bottom'].set_position(('data', 0))
    # 设置 y 轴的刻度位置在左侧
    ax.yaxis.set_ticks_position('left')
    # 设置左侧边框位置在 x=0 的位置
    ax.spines['left'].set_position(('data', 0))
    # 定义一个点的 x 坐标为 1
    x0 = 1
    # 计算点的 y 坐标
    y0 = 2 * x0 + 1
    # 在图中绘制从 (x0, 0) 到 (x0, y0) 的虚线
    plt.plot([x0, x0], [0, y0], 'k--', linewidth=2.5)
    # 在图中标记点 (x0, y0)，大小为 50，颜色为蓝色
    plt.scatter([x0], [y0], s=50, color='b')
    # 对标记的点 (x0, y0) 添加注释
    plt.annotate(r'$2x+1=%s$' % y0, xy=(x0, y0), xycoords='data', xytext=(+30, -30),
                 textcoords='offset points', fontsize=16,
                 arrowprops=dict(arrowstyle='->', connectionstyle="arc3,rad=.2"))
    # 在图中 (-3.7, 3) 的位置添加文本
    plt.text(-3.7, 3, '这是一个中文标注',
             fontdict={'size': 16, 'color': 'r'})
    # 显示图形
    plt.show()


def figure8_2():
    # 使用 numpy 创建 x 范围从 -3 到 3 的线性空间，共 50 个点
    x = np.linspace(-3, 3, 50)
    # 定义函数 y = 2x + 1
    y = 2 * x + 1

    # 创建图形，编号为 1，大小为 8x5
    plt.figure(num=1, figsize=(8, 5))
    # 绘制 x 和 y 的图形
    plt.plot(x, y)
    # 获取当前轴域
    ax = plt.gca()
    # 设置图形的右边框和上边框为不显示
    ax.spines['right'].set_color('none')
    ax.spines['top'].set_color('none')
    # 设置 x 轴的刻度位置在底部
    ax.xaxis.set_ticks_position('bottom')
    # 设置底部边框位置在 y=0 的位置
    ax.spines['bottom'].set_position(('data', 0))
    # 设置 y 轴的刻度位置在左侧
    ax.yaxis.set_ticks_position('left')
    # 设置左侧边框位置在 x=0 的位置
    ax.spines['left'].set_position(('data', 0))
    # 定义一个点的 x 坐标为 1
    x0 = 1
    # 计算点的 y 坐标
    y0 = 2 * x0 + 1
    # 在图中绘制从 (x0, 0) 到 (x0, y0) 的虚线
    plt.plot([x0, x0], [0, y0], 'k--', linewidth=2.5)
    # 在图中标记点 (x0, y0)，大小为 50，颜色为蓝色
    plt.scatter([x0], [y0], s=50, color='b')
    # 对标记的点 (x0, y0) 添加注释
    plt.annotate(r'$2x+1=%s$' % y0, xy=(x0, y0), xycoords='data', xytext=(+30, -30),
                 textcoords='offset points', fontsize=16,
                 arrowprops=dict(arrowstyle='->', connectionstyle="arc3,rad=.2"))
    # 在图中 (-3.7, 3) 的位置添加文本
    plt.text(-3.7, 3, r'$This\ is\ the\ some\ text. \mu\ \sigma_i\ \alpha_t$',
             fontdict={'size': 16, 'color': 'r'})
    # 显示图形
    plt.show()


def figure9():
    # 使用 np.linspace 创建一个从-3到3的等差数列，包含50个元素
    x = np.linspace(-3, 3, 50)
    # 定义函数 y = 0.1 * x
    y = 0.1 * x

    # 创建一个新的图形窗口
    plt.figure()
    # 绘制 x 和 y，设置线条宽度为10，通过 zorder 设置绘制顺序为1
    plt.plot(x, y, linewidth=10, zorder=1)
    # 设置 y 轴的显示范围
    plt.ylim(-2, 2)
    # 获取当前的 Axes 对象 ax
    ax = plt.gca()
    # 将右侧边框颜色设置为无，即不显示
    ax.spines['right'].set_color('none')
    # 将顶部边框颜色设置为无，即不显示
    ax.spines['top'].set_color('none')
    # 设置 x 轴的刻度位置在下方
    ax.xaxis.set_ticks_position('bottom')
    # 设置底部边框的位置，将其设置在数据坐标0的位置
    ax.spines['bottom'].set_position(('data', 0))
    # 设置 y 轴的刻度位置在左侧
    ax.yaxis.set_ticks_position('left')
    # 设置左侧边框的位置，将其设置在数据坐标0的位置
    ax.spines['left'].set_position(('data', 0))
    # 遍历所有的 x 和 y 轴的刻度标签
    for label in ax.get_xticklabels() + ax.get_yticklabels():
        # 设置标签的字体大小为12
        label.set_fontsize(12)
        # 为标签设置背景盒子，设置背景色为白色，边框色为无，透明度为0.7，通过 zorder 设置绘制顺序为2
        label.set_bbox(dict(facecolor='white', edgecolor='None', alpha=0.7, zorder=2))

    # 显示图形
    plt.show()


def print_hi(name):
    print(f'Hi, {name}')
    print("figure 绘图主要看代码注释和运行后的图像。")
    # 查看系统字体
    # font_query()
    figure1()
    figure2()
    figure3()
    figure4()
    # 调整名字和间隔（刻度）
    figure5()
    # 设置坐标轴2
    # 设置不同名字和位置,调整坐标轴
    figure6()
    # Legend 图例,调整位置和名称
    figure7()
    # Annotation 标注
    figure8_1()
    figure8_2()
    # tick 能见度,透明度
    figure9()


if __name__ == '__main__':
    print_hi('常规用法')
