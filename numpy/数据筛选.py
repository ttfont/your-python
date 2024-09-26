# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
import numpy as np


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press ⌘F8 to toggle the breakpoint.

    # 获取单个数据
    a = np.array([1, 2, 3])
    print("a[0]:", a[0])
    print("a[1]:", a[1])
    # 获取多个数据
    print("a[[0,1]]: ", a[[0, 1]])
    print("a[[1,1,0]]: ", a[[1, 1, 0]])
    print()
    # 二维或者多维数据
    b = np.array([
        [1, 2, 3, 4],
        [5, 6, 7, 8],
        [9, 10, 11, 12]
    ])

    # 选第 2 行所有数
    print("b[1]: ", b[1])

    # 选第 2 行，第 1 列的数
    print("b[1,0]: ", b[1, 0])

    # 这个看着有点纠结，如果对应到数据，
    # 第一个拿的是数据位是 [1,2]
    # 第二个拿的是 [0,3]
    print("b[[1,0],[2,3]]: ",
          b[[1, 0], [2, 3]])
    # 第一个列表 [1, 0] 指定行，第二个列表 [2, 3] 指定列，
    # 因此结果是选取 b[1, 2] 和 b[0, 3]，输出为[7, 4]。
    print()
    # 切片划分 批量获取数据
    a = np.array([1, 2, 3])
    print("a[0:2]： ", a[0:2])
    print("a[1:]： ", a[1:])
    # a[-2:]：选择从倒数第二个元素开始到结束的所有元素，输出[2, 3]。这里 -2 表示从数组的后面开始数，所以选择了第二个和第三个元素。
    print("a[-2:]： ", a[-2:])
    print()
    # 多维数据上
    b = np.array([
        [1, 2, 3, 4],
        [5, 6, 7, 8],
        [9, 10, 11, 12]
    ])

    print("b[:2]: ", b[:2])
    print("b[:2, :3]: ", b[:2, :3])
    print("b[1:3, -2:]: ", b[1:3, -2:])
    print()
    # 条件筛选
    # a 数据中，大于 7 的数据
    a = np.array([
        [1, 2, 3, 4],
        [5, 6, 7, 8],
        [9, 10, 11, 12]
    ])
    print(a[a > 7])
    print()
    # a[这里放 True/False bool数据] ，condition是一个布尔数组
    condition = a > 7
    print(condition)
    print(a[condition])
    print()
    # 修改满足条件的数据 np.where
    condition = a > 7
    print(np.where(condition, -1, a))
    print()
    condition = a > 7
    b = -a - 1
    # 原数组 a 中大于 7 的元素被保留，其余元素被替换为 b 中的对应值
    print(np.where(condition, a, b))


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('数据筛选')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
