# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
import pandas as pd
import matplotlib.pyplot as plt


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press ⌘F8 to toggle the breakpoint.
    # https://www.kaggle.com/datasets/imdevskp/corona-virus-report
    df = pd.read_csv("data/data_analysis.csv")
    # print(df)
    print(df.head())
    print()
    # 某日所有数据
    print("日期列表摘取：", df["Date"][:4])
    print("日期->索引转换：\n", df[df["Date"] == "2020-02-03"])
    # 累积 Confirmed 病例
    confirmed0124 = df.loc[df["Date"] == "2020-01-24", "Confirmed"]
    print("截止 1 月 24 日的累积确诊数：", confirmed0124.values)
    # 新增 death
    result = df.loc[df["Date"] == "2020-07-23", "New deaths"]
    print("截止 7 月 23 日的新增死亡数：", result.values)
    # 总增长数
    date = pd.to_datetime(df["Date"])
    date_range = (date >= "2020-01-25") & (date <= "2020-07-22")
    new_cases = df.loc[date_range, "New cases"]
    overall = new_cases.sum()
    print("共新增：", overall)
    # 使用累积病例
    confirmed = df.loc[:, "Confirmed"]
    conf_0722 = confirmed.loc[df["Date"] == "2020-07-22"].values
    conf_0125 = confirmed.loc[df["Date"] == "2020-01-25"].values
    print(conf_0722, conf_0125)
    overall2 = conf_0722 - conf_0125
    print("共新增：", overall2)
    # 数据不相等，找出差异数据
    confirmed = df["Confirmed"]
    new_cases = df["New cases"]
    idx_0722 = df.loc[df["Date"] == "2020-07-22"].index.item()
    idx_0125 = df.loc[df["Date"] == "2020-01-25"].index.item()

    for i in range(idx_0125, idx_0722 + 1):
        diff = new_cases.iloc[i] - (confirmed.iloc[i] - confirmed.iloc[i - 1])
        if diff != 0:
            print("date index:", i, ";差异：", diff)
    # 恢复比例
    ratio = df["New cases"] / df["New recovered"]
    print("比例样本：", ratio[:5])
    # 在数据中作为除数的数据有0，计算结果给出的是 NaN
    print(df.loc[0, "New cases"])
    print(df.loc[0, "New recovered"])

    not_zero_mask = df["New recovered"] != 0
    print(not_zero_mask)
    ratio = df.loc[not_zero_mask, "New cases"] / df.loc[not_zero_mask, "New recovered"]

    # 平均比例, 标准差
    ratio_mean = ratio.mean()
    ratio_std = ratio.std()
    print("平均比例：", ratio_mean, "；标准差：", ratio_std)

    # 可视化数据
    # 确诊的变化
    df["New cases"].plot()
    plt.show()
    print(df.loc[50, "Date"])
    # 死亡率变化
    df["Deaths / 100 Cases"].plot()
    plt.show()


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('数据分析')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
