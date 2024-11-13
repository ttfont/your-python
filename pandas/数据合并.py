# This is a sample Python script.
import pandas as pd


# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press ⌘F8 to toggle the breakpoint.
    # 拼接Concat
    df1 = pd.DataFrame({
        "A": ["A0", "A1", "A2", "A3"],
        "B": ["B0", "B1", "B2", "B3"],
        "C": ["C0", "C1", "C2", "C3"],
        "D": ["D0", "D1", "D2", "D3"],
    }, index=[0, 1, 2, 3], )
    print(df1)

    df2 = pd.DataFrame({
        "A": ["A4", "A5", "A6", "A7"],
        "B": ["B4", "B5", "B6", "B7"],
        "C": ["C4", "C5", "C6", "C7"],
        "D": ["D4", "D5", "D6", "D7"],
    }, index=[4, 5, 6, 7], )
    print(df2)

    df3 = pd.DataFrame({
        "A": ["A8", "A9", "A10", "A11"],
        "B": ["B8", "B9", "B10", "B11"],
        "C": ["C8", "C9", "C10", "C11"],
        "D": ["D8", "D9", "D10", "D11"],
    }, index=[8, 9, 10, 11], )
    print(df3)
    print()
    # 相同的 column 名拼接
    print(pd.concat([df1, df2, df3]))
    all_classes = pd.concat(
        [df1, df2, df3],
        keys=["x", "y", "z"])
    print(all_classes)

    print(all_classes.loc["y"])
    # pd.concat 默认是上下拼接的，也可以进行左右拼接。
    df4 = pd.DataFrame({
        "B": ["B2", "B3", "B6", "B7"],
        "D": ["D2", "D3", "D6", "D7"],
        "F": ["F2", "F3", "F6", "F7"],
    }, index=[2, 3, 6, 7], )

    # 外拼接
    print(pd.concat([df1, df4], axis=1), )
    # 内拼接
    print(pd.concat([df1, df4], axis=1, join="inner"))
    # 忽略数据索引
    print(pd.concat([df1, df4], ignore_index=True, sort=False))
    # 使用 concat 添加新的数据向右添加
    new_col = pd.Series(["X0", "X1", "X2", "X3"], name="X")
    print(pd.concat([df1, new_col], axis=1))
    print()
    # 向下添加
    new_row = pd.Series(["X0", "X1", "X2", "X3"], index=["A", "B", "C", "D"])
    print(new_row.to_frame())
    print(new_row.to_frame().T)
    print(pd.concat([df1, new_row.to_frame().T], ignore_index=True))

    # 融合Merge, merge 只做左右拼接
    left = pd.DataFrame({
        "key": ["K0", "K1", "K2", "K3"],
        "A": ["A0", "A1", "A2", "A3"],
        "B": ["B0", "B1", "B2", "B3"],
    })

    right = pd.DataFrame({
        "key": ["K0", "K1", "K2", "K3"],
        "C": ["C0", "C1", "C2", "C3"],
        "D": ["D0", "D1", "D2", "D3"],
    })

    print(pd.merge(left, right, on="key"))
    print()
    left = pd.DataFrame({
        "key1": ["K0", "K0", "K1", "K2"],
        "key2": ["K0", "K1", "K0", "K1"],
        "A": ["A0", "A1", "A2", "A3"],
        "B": ["B0", "B1", "B2", "B3"],
    })

    right = pd.DataFrame({
        "key1": ["K0", "K1", "K1", "K2"],
        "key2": ["K0", "K0", "K0", "K0"],
        "C": ["C0", "C1", "C2", "C3"],
        "D": ["D0", "D1", "D2", "D3"],
    })

    # 默认是 "inner"
    # print(pd.merge(left, right, on=["key1", "key2"]))
    print(pd.merge(left, right, how="inner", on=["key1", "key2"]))
    print(pd.merge(left, right, how="outer", on=["key1", "key2"]))
    print(pd.merge(left, right, how="left", on=["key1", "key2"]))
    print(pd.merge(left, right, how="right", on=["key1", "key2"]))
    print(pd.merge(left, right, how="cross"))

    # join
    left = pd.DataFrame({
        "A": ["A0", "A1", "A2"],
        "B": ["B0", "B1", "B2"]
    }, index=["K0", "K1", "K2"])

    right = pd.DataFrame({
        "C": ["C0", "C2", "C3"],
        "D": ["D0", "D2", "D3"]
    }, index=["K0", "K2", "K3"])

    # join 默认 how="left"
    print(left.join(right))
    print()
    print(left.join(right, how="left"))
    print(left.join(right, how="right"))
    print(left.join(right, how="inner"))
    print(left.join(right, how="outer"))
    print(left.join(right, how="cross"))
    print()
    left = pd.DataFrame({
        "A": ["A0", "A1", "A2", "A3"],
        "B": ["B0", "B1", "B2", "B3"],
        "key": ["K0", "K1", "K0", "K1"],
    })

    right = pd.DataFrame({
        "C": ["C0", "C1"],
        "D": ["D0", "D1"]
    }, index=["K0", "K1"])

    print(left.join(right, on="key"))


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('数据合并')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
