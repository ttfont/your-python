# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press ⌘F8 to toggle the breakpoint.
    # 找到NaN数据
    # pd.isna(), pd.notna()
    # NaN的影响
    # 移除NaN
    # df.dropna()
    # 填充NaN
    # df.fillna()
    # 不符合范围的值
    # df.clip()

    # 找到NaN数据
    df = pd.DataFrame([[1, None], [np.nan, 4]])
    print(df)
    print(df.isna())
    print(~df.isna())
    print(df.notna())

    # NaN的影响
    # pandas 是不考虑 NaN 值的，也就是说不会把 NaN 带入运算，如果考虑 NaN 的话， mean 就会是 (1+1)/3 和 (4+4)/3 因为有三个数据。
    df = pd.DataFrame({
        "a": [1, None, 1],
        "b": [np.nan, 4, 3]
    })
    print(df)
    print("skipped NaN:\n", df.mean(axis=0))
    print("\n\nnot skipped:\n", df.mean(axis=0, skipna=False))

    # 移除NaN
    df = pd.DataFrame({
        "a": [1, None, 3],
        "b": [4, 5, 6]
    })
    print(df)
    print(df.dropna(axis=0))
    print(df.dropna(axis=1))
    print()
    # 填充NaN
    df = pd.DataFrame({
        "a": [1, None, 3],
        "b": [4, 5, 6]
    })
    print(df)
    a_mean = df["a"].mean()
    print(a_mean)
    new_col = df["a"].fillna(a_mean)
    print(new_col)
    df["a"] = new_col
    print(df)
    print()
    # 有规律的数据填充
    # 使用fillna填充
    df = pd.DataFrame({
        "a": [1, None, 3, None],
        "b": [4, 8, 12, 12]
    })
    print(df)
    a_nan = df["a"].isna()
    print(a_nan)
    a_new_value = df["b"][a_nan] / 4
    print(a_new_value)
    new_col = df["a"].fillna(a_new_value)
    print(new_col)
    df["a"] = new_col
    print(df)
    print()
    # 使用 loc 填充
    df = pd.DataFrame({
        "a": [1, None, 3, None],
        "b": [4, 8, 12, 12]
    })
    a_nan = df["a"].isna()
    print(a_nan)
    print(df.loc[a_nan, "a"])
    print(df["b"][a_nan] / 4)
    df.loc[a_nan, "a"] = df["b"][a_nan] / 4
    print(df)

    # 不符合范围的值
    df = pd.DataFrame({
        "a": [1, 1, 2, 1, 2, 40, 1, 2, 1],
    })
    df.plot()
    df["a"] = df["a"].clip(lower=0, upper=3)
    df.plot()
    plt.show()


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('异常数据处理')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
