# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
import pandas as pd
import numpy as np


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press ⌘F8 to toggle the breakpoint.
    # 主要方法
    # 选Column
    # loc
    # iloc
    # loc和iloc混搭
    # 条件过滤筛选
    # Series和DataFrame类似

    # 多种选取方式
    # 构建Excel 型的表格数据

    data = np.arange(-12, 12).reshape((6, 4))
    df = pd.DataFrame(
        data,
        index=list("abcdef"),
        columns=list("ABCD"))
    print(df)
    # 选Column
    print(df["B"])
    # 多选几个列
    print("numpy:\n", data[:, [2, 1]])
    print("\ndf:\n", df[["C", "B"]])

    # loc，像Excel一样取数
    # numpy取数
    print(data[2:3, 1:3])
    # DataFrame 取数
    print(df.loc["c":"d", "B":"D"])
    # 单行取数
    print("numpy:\n", data[[3, 1], :])
    print("\ndf:\n", df.loc[["d", "b"], :])
    # 不按顺序设置索引
    df2 = pd.DataFrame(
        data,
        index=list("beacdf"),
        columns=list("ABCD"))
    print(df2)
    print(df2.loc["e":"c"])

    # iloc，按数据位置取数
    print("numpy:\n", data[2:3, 1:3])
    print("\ndf:\n", df.iloc[2:3, 1:3])
    print("numpy:\n", data[[3, 1], :])
    print("\ndf:\n", df.iloc[[3, 1], :])

    # loc和iloc混搭
    # 序号索引转换成 .loc 的标签索引，根据索引获取标签
    row_labels = df.index[2:4]
    print("row_labels:\n", row_labels)
    print("\ndf:\n", df.loc[row_labels, ["A", "C"]])
    # labels 取 Column
    col_labels = df.columns[[0, 3]]
    print("col_labels:\n", col_labels)
    print("\ndf:\n", df.loc[row_labels, col_labels])
    # 把索引找出来放到 iloc 里用，根据标签获取索引
    col_index = df.columns.get_indexer(["A", "B"])
    print("col_index:\n", col_index)
    print("\ndf:\n", df.iloc[:2, col_index])
    # label 对应的 index
    print(df.index.get_indexer(["a", "b"]))

    # 条件过滤筛选
    # 选在 A Column 中小于 0 的那些数据
    print(df[df["A"] < 0])
    # 选在第一行数据不小于 -10 的数据 ，~ 来表示 非 或者 取反，第二种是直接用 >=-10 来筛选。
    print("~:\n", df.loc[:, ~(df.iloc[0] < -10)])
    print("\n>=:\n", df.loc[:, df.iloc[0] >= -10])
    # 选在第一行数据不小于 - 10 或小于 - 11 的数据
    # 或 | 来表示 or 的意思, & 表述 and
    print()
    i0 = df.iloc[0]
    print(i0)
    print(df.loc[:, ~(i0 < -10) | (i0 < -11)])
    print(~(df.iloc[0] < -10))
    # 基于标签或条件来选择数据，应该使用.loc；基于位置或已知的行列索引列表来选择数据，应该使用.iloc。

    # Series和DataFrame类似
    list_data = list(range(-4, 4))
    s = pd.Series(
        list_data,
        index=list("abcdefgh"))
    print(s)
    # 标签筛选数据.loc
    print(s.loc[["a", "g", "c"]], "\n")
    print(s.loc["c": "f"])
    # index 筛选数据.iloc
    print(s.iloc[[3, 1, 5]], "\n")
    print(s.iloc[2: 4])
    # iloc 和 loc 互相混用
    print(s.iloc[s.index.get_indexer(["c", "d"])], "\n")
    print(s.loc[s.index[[3, 2]]])
    # 按条件过滤筛选
    print(s.loc[s < 3], "\n")
    print(s.loc[(s < 0) & (s > -2)], "\n")
    print(s.loc[(s < 0) | (s > 2)], "\n")
    #  Numpy数据可以和Pandas数据 互转


if __name__ == '__main__':
    print_hi('选取数据')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
