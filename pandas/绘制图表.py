# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press ⌘F8 to toggle the breakpoint.
    # 散点图Scatter
    n = 1024  # data size
    df = pd.DataFrame({
        "x": np.random.normal(0, 1, n),
        "y": np.random.normal(0, 1, n),
    })
    color = np.arctan2(df["y"], df["x"])
    df.plot.scatter(x="x", y="y", c=color, s=60, alpha=.5, cmap="rainbow")

    # 折线图Plot
    n = 20  # data size
    x = np.linspace(-1, 1, n)
    y = x * 2 + 0.4 + np.random.normal(0, 0.3, n)
    df = pd.DataFrame({
        "x": x,
        "y": y,
    })
    df.plot(x="x", y="y", alpha=.5, c="r")

    n = 20  # data size
    x = np.linspace(-1, 1, n)
    y1 = x * -1 - 0.1 + np.random.normal(0, 0.3, n)
    y2 = x * 2 + 0.4 + np.random.normal(0, 0.3, n)
    df = pd.DataFrame({
        "x": x,
        "y1": y1,
        "y2": y2,
    })
    df.plot(x="x", y=["y1", "y2"], alpha=.5)

    # 条形图Bar
    df = pd.DataFrame(np.random.rand(5, 3), columns=["a", "b", "c"])
    df.plot.bar()

    df.plot.bar(stacked=True)

    df.plot.barh()

    # 分布图Hist
    df = pd.DataFrame({"a": np.random.randn(1000)})
    df.plot.hist()

    df = pd.DataFrame(
        {
            "a": np.random.randn(1000) + 1,
            "b": np.random.randn(1000),
            "c": np.random.randn(1000) - 4,
        }
    )

    df.plot.hist(alpha=0.5, bins=30)

    # 饼图Pie
    df = pd.DataFrame(
        {"boss": np.random.rand(4)},
        index=["meeting", "supervise", "teaching", "team building"],
    )
    df.plot.pie(y="boss", figsize=(7, 7))


    df = pd.DataFrame(
        {
            "bigBoss": np.random.rand(4),
            "smallBoss": np.random.rand(4),
        },
        index=["meeting", "supervise", "teaching", "team building"],
    )
    df.plot.pie(subplots=True, figsize=(9, 9), legend=False)
    # 面积图Area
    df = pd.DataFrame(
        np.random.rand(10, 4),
        columns=["a", "b", "c", "d"]
    )
    df.plot.area()
    plt.show()
    df.plot.area(stacked=False)
    plt.show()
    # https://pandas.pydata.org/pandas-docs/stable/user_guide/visualization.html

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('绘制图表')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
