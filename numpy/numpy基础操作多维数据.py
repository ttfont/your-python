# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
import numpy as np


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press ⌘F8 to toggle the breakpoint.

    # 创建多维数据
    cars = np.array([5, 10, 12, 6])
    print("数据：", cars, "\n维度：", cars.ndim)
    # 创建二维数据
    cars = np.array([
        [5, 10, 12, 6],
        [5.1, 8.2, 11, 6.3],
        [4.4, 9.1, 10, 6.6]
    ])
    print("数据：\n", cars, "\n维度：", cars.ndim)
    print()
    # 创建三维数据
    cars = np.array([
        [
            [5, 10, 12, 6],
            [5.1, 8.2, 11, 6.3],
            [4.4, 9.1, 10, 6.6]
        ],
        [
            [6, 11, 13, 7],
            [6.1, 9.2, 12, 7.3],
            [5.4, 10.1, 11, 7.6]
        ],
    ])

    print("总维度：", cars.ndim)
    print("场地 1 数据：\n", cars[0], "\n场地 1 维度：", cars[0].ndim)
    print("场地 2 数据：\n", cars[1], "\n场地 2 维度：", cars[1].ndim)
    # 创建多维数据，自己动手丰衣足食。
    print()
    # 添加数据
    cars1 = np.array([5, 10, 12, 6])
    cars2 = np.array([5.2, 4.2])
    cars = np.concatenate([cars1, cars2])
    print(cars)

    print()
    # 增加维度
    test1 = np.array([5, 10, 12, 6])
    test2 = np.array([5.1, 8.2, 11, 6.3])

    # 首先需要把它们都变成二维，下面这两种方法都可以加维度
    test1 = np.expand_dims(test1, 0)
    test2 = test2[np.newaxis, :]

    print("test1加维度后 ", test1)
    print("test2加维度后 ", test2)

    # test3 = np.expand_dims(test1, 0)
    # print("test3加维度后 ", test3)

    # 然后再在第一个维度上叠加
    all_tests = np.concatenate([test1, test2])
    print("括展后\n", all_tests)
    print()
    # 合并数据
    print("第一维度叠加：\n", np.concatenate([all_tests, all_tests], axis=0))
    print("第二维度叠加：\n", np.concatenate([all_tests, all_tests], axis=1))
    # 维度对齐的可以进行合并操作
    print()
    a = np.array([
        [1, 2, 3],
        [4, 5, 6]
    ])
    b = np.array([
        [7, 8],
        [9, 10]
    ])

    print(np.concatenate([a, b], axis=1))  # 这个没问题
    # print(np.concatenate([a,b], axis=0))  # 这个会报错
    print()
    # 指定方向合并，np.vstack 和 np.hstack 处理二维数据时非常方便，也可以在其他多维数据上使用
    a = np.array([
        [1, 2],
        [3, 4]
    ])
    b = np.array([
        [5, 6],
        [7, 8]
    ])
    print("竖直合并\n", np.vstack([a, b]))
    print("水平合并\n", np.hstack([a, b]))
    print()
    # 观察形态
    cars = np.array([
        [5, 10, 12, 6],
        [5.1, 8.2, 11, 6.3],
        [4.4, 9.1, 10, 6.6]
    ])

    count = 0
    for i in range(len(cars)):
        for j in range(len(cars[i])):
            count += 1
    print("总共多少测试数据：", count)
    print("总共多少测试数据：", cars.size)

    print("第一个维度：", cars.shape[0])
    print("第二个维度：", cars.shape[1])
    print("所有维度：", cars.shape)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('numpy 基础操作多维数据')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
