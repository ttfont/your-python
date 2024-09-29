# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
import numpy as np
import time
import random


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press ⌘F8 to toggle the breakpoint.

    # 创建统一数据
    # 初始化 Array 全 0 或者全 1 的数据
    zeros = np.zeros([2, 3])
    print("zeros:\n", zeros)

    ones = np.ones([3, 2])
    print("\nones:\n", ones)
    # 初始化指定数值
    nines = np.full([2, 3], 9)
    print(nines)

    data = np.array([
        [1, 2, 3],
        [4, 5, 6]
    ], dtype=np.int64)

    ones = np.ones(data.shape, dtype=data.dtype)
    # 复刻形状和类型
    # 返回与给定数组具有相同形状和类型的数组，初始化值为 1
    ones_like = np.ones_like(data)

    print("ones:", ones.shape, ones.dtype)
    print("ones_like:", ones_like.shape, ones_like.dtype)
    print("ones_like value:\n", ones_like)
    print(np.zeros_like(data))
    print(np.full_like(data, 6))
    # 创建规则数据
    print("python range:", list(range(5)))
    print("numpy arange:", np.arange(5))

    print("python range:", list(range(3, 10, 2)))
    print("numpy arange:", np.arange(3, 10, 2))
    # (start, end, num)
    print("linspace:", np.linspace(-1, 1, 5))
    print("5 segments:", np.linspace(-1, 1, 5, endpoint=False))

    # 快速创建再添加值
    print(np.empty([4, 3]))

    t0 = time.time()

    for _ in range(1000):
        _ = np.ones([100, 100])

    t1 = time.time()
    for _ in range(1000):
        _ = np.empty([100, 100])

    t2 = time.time()
    print("ones time:", t1 - t0)
    print("empty time:", t2 - t1)
    print()
    # 快速初始化对应形状的数据
    empty1 = np.empty([2, 3], dtype=float)
    print("empty before:\n", empty1)
    data = np.arange(6).reshape([2, 3])
    print(data)
    for i in range(data.shape[0]):
        for j in range(data.shape[1]):
            empty1[i, j] = data[i, j] * random.random()
    print("empty after:\n", empty1)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('标准数据生成')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
