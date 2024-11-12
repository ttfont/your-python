# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
import numpy as np
import pandas as pd
import datetime
import matplotlib.pyplot as plt
import pytz


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press ⌘F8 to toggle the breakpoint.

    # 读时间序列数据

    df = pd.DataFrame({
        "time": ["2022/03/12", "2022/03/13", "2022/03/14"],
        "value": [1, 2, 3]
    })
    print(df)
    print("\n\ntime:\n", df["time"])
    # dtype:object
    # 转成 datetime64
    print(pd.to_datetime(df["time"]))
    print(pd.to_datetime(
        ["2022/03/12", "2022.03.13", "14/03/2022"], format='mixed'))
    print(pd.to_datetime(
        [
            "1@21@2022%%11|11|32",
            "12@01@2022%%44|02|2",
            "4@01@2022%%14|22|2"
        ],
        format="%m@%d@%Y%%%%%S|%H|%M"))
    # https://docs.python.org/3/library/datetime.html#strftime-and-strptime-behavior
    # %m 月
    # %d 日
    # %Y 年的全称
    # %% 比配一个 %
    # %S 秒
    # %H 时
    # %M 分

    # 自建时间序列
    start = datetime.datetime(2022, 3, 12)
    end = datetime.datetime(2022, 3, 18)

    index = pd.date_range(start, end)
    print(index)

    print(
        "range(1, 10, 2)\n",
        list(range(1, 10, 2))
    )
    print(
        "\n\npd.date_range()\n",
        pd.date_range(start, end, freq="48h")
    )
    print(
        "np.linspace(-1, 1, 5)\n",
        np.linspace(-1, 1, 5)
    )
    # 均匀分布
    print(
        "\n\npd.date_range(start, end, periods=5)\n",
        pd.date_range(start, end, periods=5)
    )
    # 选取时间
    start = datetime.datetime(2022, 3, 1)
    end = datetime.datetime(2022, 5, 3)

    rng = pd.date_range(start, end)
    ts = pd.Series(np.random.randn(len(rng)), index=rng)
    print()
    print(ts)
    print()
    print(ts.index)
    print(ts.plot())
    plt.show()
    # 显示某一周时间数据
    ts[1:8].plot()
    plt.show()
    # 时间本身分片
    t1 = datetime.datetime(2022, 3, 12)
    t2 = datetime.datetime(2022, 3, 18)
    ts[t1: t2].plot()
    plt.show()
    ts["2022-03-12": "2022-03-18"].plot()
    plt.show()
    # 按月按年取
    ts["2022-03"].plot()
    plt.show()
    print()
    # 时间运算
    # 加一周
    rng = pd.date_range("2022-01-01", "2022-01-07")
    print(rng + pd.Timedelta(weeks=1))
    print(rng + 2 * pd.Timedelta(days=3))
    rng = pd.date_range("2022-04-08", "2022-04-11")
    print(rng.dayofyear)

    print(rng.strftime("%m/%d/%Y"))
    # https://pandas.pydata.org/docs/reference/arrays.html#datetime-data

    # 时区
    rng = pd.date_range("2022-01-08", "2022-01-11")
    print(rng.tz is None)
    s = pd.to_datetime(
        ["2022/03/12 22:11", "2022/03/12 12:11", "2022/03/12 2:11"]
    )
    s_us = s.tz_localize("America/New_York")
    print(s_us)
    s_cn = s_us.tz_convert("Asia/Shanghai")
    print(s_cn)
    print(pytz.country_timezones('CN'))
    rng = pd.date_range(
        "2022-01-08", "2022-01-11",
        tz="America/New_York")
    print(rng)
    # https://pandas.pydata.org/docs/user_guide/timeseries.html


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('时间数据')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
