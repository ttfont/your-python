# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
from matplotlib import pyplot as plt
from matplotlib import animation
import numpy as np


def animate(i, line, x):
    # 更新线条的Y数据，使得正弦波随时间动态变化
    line.set_ydata(np.sin(x + i / 10.0))
    return line,


# 初始化动画，设置初始状态
def init(line, x):
    # 初始化线条数据，使其不显示任何东西（通过mask实现）
    line.set_ydata(np.ma.array(x, mask=True))
    return line,


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press ⌘F8 to toggle the breakpoint.

    # 创建图形和坐标轴
    fig, ax = plt.subplots()
    x = np.arange(0, 2 * np.pi, 0.01)  # 创建x数据，用于绘制正弦波
    line, = ax.plot(x, np.sin(x))  # 绘制初始正弦波

    # 创建动画
    ani = animation.FuncAnimation(fig=fig,
                                  func=lambda i: animate(i, line, x),  # 指定动画函数
                                  frames=np.arange(1, 200),  # 设置动画帧数
                                  init_func=lambda: init(line, x),  # 指定初始化函数
                                  interval=20,  # 设置更新间隔（毫秒）
                                  blit=False)  # blit=True时仅重绘变化部分以提高效率，但在此设为False以保证兼容性
    # 保存动画
    ani.save('basic_animation.mp4', fps=30, extra_args=['-vcodec', 'libx264'])

    # 显示图形
    plt.show()


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('Animation 动画')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
