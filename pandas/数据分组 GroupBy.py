# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
import pandas as pd
import numpy as np


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press ⌘F8 to toggle the breakpoint.
    # 分组

    df = pd.DataFrame(
        [
            ("小红", "哈利波特", 80),
            ("小明", "蜘蛛侠", 72),
            ("小红", "雷神", 83),
            ("小红", "蜘蛛侠", 45),
            ("小明", "超人", 57),
        ],
        columns=("人", "人物", "评价"),
    )
    print(df)
    grouped = df.groupby("人")
    print(grouped)
    print(grouped.groups)
    print(df.iloc[grouped.groups["小红"]])
    print(grouped.get_group("小红"))

    # 调用分好的组
    print(grouped.first())
    print(grouped.last())
    print(grouped.sum())
    print(grouped.get_group("小红")["评价"].sum())

    # 循环处理
    for name, group in grouped:
        print("name:", name)
        print("group:", group)
    print()
    # 多列分组
    df = pd.DataFrame(
        [
            ("小红", "哈利波特", 80),
            ("小明", "蜘蛛侠", 72),
            ("小红", "雷神", 83),
            ("小红", "雷神", 90),
            ("小红", "蜘蛛侠", 45),
            ("小明", "超人", 57),
        ],
        columns=("人", "人物", "评价"),
    )
    print(df)
    print(df.groupby(["人", "人物"]).groups)
    print(df.groupby(["人", "人物"]).get_group(("小红", "雷神")))
    print()
    # 聚合计算
    grouped = df.groupby("人")
    print(grouped.groups)
    print(grouped.aggregate(np.sum))
    print(grouped.get_group("小红")["评价"].aggregate(np.sum))
    print(grouped["评价"].agg([np.sum, np.mean, np.std]))
    print(grouped["评价"].agg([np.sum, np.mean, np.std]).rename(columns={"sum": "合计", "mean": "均值", "std": "标准差"}))


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('数据分组 GroupBy')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
