# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
import pandas as pd
import numpy as np


def func01(x):
    return x[0] * 2, x[1] * -1


def func02(x):
    return x["A"] * 4


def func03(r):
    return r[2] * 4


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press ⌘F8 to toggle the breakpoint.
    # 筛选赋值运算

    data = np.arange(-12, 12).reshape((6, 4))
    df = pd.DataFrame(
        data,
        index=list("abcdef"),
        columns=list("ABCD"))
    print(df)
    df["A"] *= 0
    print(df)
    print()
    # iloc 找的是 index，loc 找的是标签。
    df.loc["a", "A"] = 100
    df.iloc[1, 0] = 200
    print(df)
    df.loc["a", :] = df.loc["a", :] * 2
    print(df)
    df["A"][df["A"] == 0] = -1
    print(df)

    # Apply方法
    df = pd.DataFrame([[4, 9]] * 3, columns=['A', 'B'])
    print(df)
    # 平方根计算
    print(np.sqrt(df))
    print(df.apply(np.sqrt))
    print(df.apply(func01, axis=1, result_type='expand'))
    # 继承原来的行和列名
    print(df.apply(func01, axis=1, result_type='broadcast'))
    print(df.apply(func02, axis=1))
    print()
    print(df)
    df["A"] = df.apply(func02, axis=1)
    print(df)
    last_row = df.apply(func03, axis=0)
    print("last_row:\n", last_row)

    df.iloc[2, :] = last_row
    print("\ndf:\n", df)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('运算方法')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
