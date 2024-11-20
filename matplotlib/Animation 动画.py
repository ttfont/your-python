# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
from matplotlib import pyplot as plt
from matplotlib import animation
import numpy as np


def animate(i, line, x):
    line.set_ydata(np.sin(x + i / 10.0))  # update the data
    return line,


# Init only required for blitting to give a clean slate.
def init(line, x):
    line.set_ydata(np.ma.array(x, mask=True))
    return line,


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press ⌘F8 to toggle the breakpoint.

    fig, ax = plt.subplots()
    x = np.arange(0, 2 * np.pi, 0.01)
    line, = ax.plot(x, np.sin(x))

    ani = animation.FuncAnimation(fig=fig,
                                  func=lambda i: animate(i, line, x),
                                  frames=np.arange(1, 200),
                                  init_func=lambda: init(line, x),
                                  interval=20,
                                  blit=False)
    # 系统未安装 ffmpeg ，请先安装 ffmpeg，如 macOS 安装，brew install ffmpeg 。
    ani.save('basic_animation.mp4', fps=30, extra_args=['-vcodec', 'libx264'])

    plt.show()


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('Animation 动画')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
