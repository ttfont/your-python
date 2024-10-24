# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
import pandas as pd
import numpy as np


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press ⌘F8 to toggle the breakpoint.
    # 数据序列Series
    # 创建
    # 转换 Numpy
    # 数据表DataFrame
    # 创建
    # 转换 Numpy
    # 数据序列Series
    l = [11, 22, 33]
    s = pd.Series(l)
    print("list:", l)
    print("series:", s)
    # 自定义索引
    s = pd.Series(l, index=["a", "b", "c"])
    print(s)
    # 一维的 Series
    # 字典转序列
    s = pd.Series({"a": 11, "b": 22, "c": 33})
    print(s)
    # numpy转序列
    s = pd.Series(np.random.rand(3), index=["a", "b", "c"])
    print(s)
    # 序列转 List 和 numpy
    print("array:", s.to_numpy())
    print("list:", s.values.tolist())

    # 数据表DataFrame
    # 二维数组变成 Pandas 的 DataFrame。
    df = pd.DataFrame([
        [1, 2],
        [3, 4]
    ])
    print(df)
    # 选择数据
    # 第 0 行，第 1 列
    # 或 第一个维度中的第 0 号，第二个维度中的第 1 号
    print(df.at[0, 1])
    # 自定义索引序号，key 会被转成 column
    df = pd.DataFrame({"col1": [1, 3], "col2": [2, 4]})
    print(df)
    # Series 转 DataFrame ，从 DataFrame 中取出一个 Column
    print(df["col1"], "\n")
    print("取出来之后的 type：", type(df["col1"]))
    # 两个 Series 拼在一起
    df = pd.DataFrame({"col1": pd.Series([1, 3]), "col2": pd.Series([2, 4])})
    print(df)
    # 自定义特殊的索引
    s = pd.Series([1.0, 2.0, 3.0], index=["a", "b", "c"])
    df = pd.DataFrame({"col1": [1, 3], "col2": [2, 4]}, index=["a", "b"])
    print(s, "\n")
    print(df)
    # 获取索引值
    print("索引：", df.index, "\n")
    print("列名：", df.columns)
    print("索引类型：", type(df.index), "\n")
    print("列名类型：", type(df.columns))
    # json数据转换成DataFrame
    my_json_data = [
        {"age": 12, "height": 111},
        {"age": 13, "height": 123}
    ]
    print(pd.DataFrame(my_json_data, index=["jack", "rose"]))
    # DataFrame 转 numpy
    df = pd.DataFrame({"col1": [1, 3], "col2": [2, 4]}, index=["a", "b"])
    print(df.to_numpy())
    # Pandas 中，Series 的一维数据，和 DataFrame 的二维数据


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('Pandas 中的数据是什么')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
