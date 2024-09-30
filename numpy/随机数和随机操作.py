# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

import random
import numpy as np


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press ⌘F8 to toggle the breakpoint.

    # 多种随机数生成
    print(random.random())
    print(random.randint(1, 10))

    # 随机生成 [0, 1) 之间的数
    dim1, dim2 = 3, 2
    print(np.random.rand(dim1, dim2))  # 你还能继续添加 dim3 或更多
    print(np.random.randn(dim1, dim2))
    print(np.random.randint(low=-3, high=6, size=10))

    # 给你施加随机
    # 对已有的数据做随机化处理，随机从一组数据中选择
    data = np.array([2, 1, 3, 4, 6])
    print("选一个：", np.random.choice(data))
    print("选多个：", np.random.choice(data, size=3))
    print("不重复地选多个(不放回)：", np.random.choice(data, size=3, replace=False))
    print("带权重地选择：", np.random.choice(data, size=10, p=[0, 0, 0, 0.2, 0.8]))
    # 将源数据洗牌重新排列，如果你想保留源数据的话，记得 np.copy(data) 备份一下
    data_copy = np.copy(data)
    np.random.shuffle(data)
    print("源数据：", data_copy)
    print("shuffled:", data)
    print()
    print("直接出乱序序列：", np.random.permutation(10))
    data = np.arange(12).reshape([6, 2])
    print(data)
    # 多维数据在第一维度上乱序，指的是这个维度的行乱序
    print("多维数据在第一维度上乱序：", np.random.permutation(data))
    # 随机分布
    # (均值，方差，size)
    print("正态分布：", np.random.normal(1, 0.2, 10))

    # (最低，最高，size)
    print("均匀分布：", np.random.uniform(-1, 1, 10))
    # 随机种子的重要性
    # seed(1) 代表的就是 1 号随机序列
    # Numpy 中的 random seed 概念，随机种子。当我们把种子固定的时候（用一个数字），同一个种子（数字）产生的随机序列就会一样
    np.random.seed(1)
    print(np.random.randint(2, 10, size=3))
    print(np.random.randint(2, 10, size=3))
    # 重新设定种子，输入不同种子随机值不一样，输入相同种子随机值一样
    np.random.seed(2)
    print(np.random.randint(2, 10, size=3))
    np.random.seed(2)
    print(np.random.randint(2, 10, size=3))
    np.random.seed(3)
    print(np.random.randint(2, 10, size=3))


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('随机数和随机操作')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
