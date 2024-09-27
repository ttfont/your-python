# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

import numpy as np


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press ⌘F8 to toggle the breakpoint.
    # 加减乘除
    l = [150, 166, 183, 170]
    for i in range(len(l)):
        l[i] += 3
    print(l)
    # 语法：map(function, iterable)
    print(list(map(lambda x: x + 3, [150, 166, 183, 170])))

    # 使用 numpy 计算
    a = np.array([150, 166, 183, 170])
    print(a + 3)
    print("a - 3:", a - 3)
    print("a * 3:", a * 3)
    print("a / 3:", a / 3)
    print()
    # 矩阵点积运算
    a = np.array([
        [1, 2],
        [3, 4]
    ])
    b = np.array([
        [5, 6],
        [7, 8]
    ])

    print(a.dot(b))
    print(np.dot(a, b))
    print()
    # 数据统计分析
    a = np.array([150, 166, 183, 170])
    print("最大：", np.max(a))
    print("最小：", a.min())
    print(a.sum())

    a = np.array([150, 166, 183, 170])
    print("累乘：", a.prod())
    print("总数：", a.size)

    a = np.array([0, 1, 2, 3])
    print("非零总数：", np.count_nonzero(a))

    month_salary = [1.2, 20, 0.5, 0.3, 2.1]
    print("平均工资：", np.mean(month_salary))
    print("工资中位数：", np.median(month_salary))

    month_salary = [1.2, 20, 0.5, 0.3, 2.1]
    print("标准差：", np.std(month_salary))
    print()
    # 特殊运算符号
    a = np.array([150, 166, 183, 170])
    name = ["张三", "李四", "王五", "赵六"]
    # 返回对应数值的索引
    high_idx = np.argmax(a)
    low_idx = np.argmin(a)
    # 返回最大值的索引
    print("{} 最高".format(name[high_idx]))
    # 返回最小值的索引
    print("{} 最矮".format(name[low_idx]))
    print()
    a = np.array([150.1, 166.4, 183.7, 170.8])
    # 向上取整
    print("ceil:", np.ceil(a))
    # 向下取整
    print("floor:", np.floor(a))
    print()
    a = np.array([150.1, 166.4, 183.7, 170.8])
    # 限制数组值在 [160, 180] 范围内
    # 将数组中小于 160 的值替换为 160，大于 180 的值替换为 180
    print("clip:", a.clip(160, 180))


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('基础运算')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
