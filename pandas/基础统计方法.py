# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

import pandas as pd
import numpy as np


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press ⌘F8 to toggle the breakpoint.
    # 日常一般用法
    # 均值中位数
    # df.mean()；df.median()
    # 累加累乘
    # df.sum()；df.prod()
    # 最大最小
    # df.max();
    # df.min()
    # 处理空值
    # df.isnull();
    # df.notnull();
    # df.dropna();
    # df.fillna()
    # 获取索引
    # df.idxmin();
    # df.idxmax()

    data = np.array([
        [1.39, 1.77, None],
        [0.34, 1.91, -0.05],
        [0.34, 1.47, 1.22],
        [None, 0.27, -0.61]
    ])
    # df = pd.DataFrame(data, index=["r0", "r1", "r2", "r3"], columns=["c0", "c1", "c2"], dtype=float)
    df = pd.DataFrame(data, index=["r0", "r1", "r2", "r3"], columns=["c0", "c1", "c2"])
    print(df)
    # 非纯数值型数据
    print(df.describe())
    # 纯数值型数据
    df1 = pd.DataFrame(np.random.random((4, 3)), columns=["c0", "c1", "c2"])
    print(df1)
    print("\ndescribe:\n", df1.describe())

    # 均值中位数,第 0 个维度
    print(df.mean())
    print(df.mean(axis=0))
    # 第 1 个维度求均值
    print(df.mean(axis=1))
    # Pandas 遇到 NaN，不计算这列、行的数据
    print()
    df = df.replace({None: np.nan})
    # df = df.dropna()
    print(df.mean(axis=0, skipna=False))
    print(df.mean(axis=1, skipna=False))
    # 最后一个为高收入人
    s = pd.Series([1000, 2000, 4000, 100000])
    print("mean():", s.mean())  # 拉高平均收入，拉高仇恨
    print("median():", s.median())  # 比较合理
    print()
    # 累加累乘
    df = pd.DataFrame(np.arange(12).reshape((4, 3)), columns=["c0", "c1", "c2"])
    print(df)
    print("sum():\n", df.sum())
    print("\nsum(axis=0):\n", df.sum(axis=0))
    print("\nsum(axis=1):\n", df.sum(axis=1))
    print("prod():\n", df.prod())
    print("\nprod(axis=0):\n", df.prod(axis=0))
    print("\nprod(axis=1):\n", df.prod(axis=1))
    # 最大最小
    print("max():\n", df.max())
    print("\nmin():\n", df.min())
    print(df.max().max())
    print(df.values.ravel().max())  # 用 Numpy 的方式运算
    print()
    # 处理空值
    # 查看数据用没有空值
    df = pd.DataFrame([[1, 2, 3, 0],
                       [3, 4, None, 1],
                       [None, None, None, None],
                       [None, 3, None, 4]],
                      columns=list("ABCD"))
    print(df)
    print("\nisnull():\n", df.isnull())  # True 就是空
    print("\nnotnull()\n", df.notnull())  # False 为空
    print("默认：\n", df.dropna())  # 默认按 axis=0，删除含有 None 的行
    print("\naxis=1:\n", df.dropna(axis=1))  # 可以换一个 axis drop
    # 除掉全为空的数据，只要有值就用
    df1 = pd.DataFrame([[None, None, None], [1, None, 3]])
    print(df1.dropna(how="all"))  # how 默认为 "any"
    # 填充 111,对空值进行填充
    print(df.fillna(111))
    # 差异化填充
    values = {"A": 0, "B": 1, "C": 2, "D": 3}
    print(df.fillna(value=values))
    # 使用新的 df 来做 nan 填充
    df2 = pd.DataFrame(np.arange(16).reshape((4, 4)), columns=list("ABCD"))
    print("df2:\n", df2)
    print("\nfillna(df2):\n", df.fillna(df2))

    # 获取索引
    df = pd.DataFrame([[1, 2, 3, 0],
                       [3, 4, None, 1],
                       [3, 5, 2, 1],
                       [3, 2, 2, 3]],
                      columns=list("ABCD"))
    print(df)
    print("\nidxmax():\n", df.idxmax())
    print("\nidxmax(skipna=False):\n", df.idxmax(skipna=False))
    print("\nidxmin():\n", df.idxmin())


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('基础统计方法')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
