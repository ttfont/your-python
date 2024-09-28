# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
import numpy as np


# 读取数据
def get_result():
    with open("csv/your_data.csv", "r", encoding="utf-8") as f:
        data = f.readlines()

    your_data = {
        "date": [],
        "data": [],
        "header": [h for h in data[0].strip().split(",")[1:]]
    }

    for row in data[1:]:
        split_row = row.strip().split(",")
        your_data["date"].append(split_row[0])
        your_data["data"].append([float(n) for n in split_row[1:]])
    return your_data


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press ⌘F8 to toggle the breakpoint.
    your_data = get_result()

    # 获取少数行数据
    print(your_data["data"][:2])
    print(your_data["date"][:5])

    # 获取指定日期数据
    date_idx = your_data["date"].index("2020-02-03")
    print("日期->索引转换：", date_idx)

    data = np.array(your_data["data"])

    for header, number in zip(your_data["header"], data[date_idx]):
        print(header, ":", number)
    # 获取指定行列数据
    row_idx = your_data["date"].index("2020-01-24")  # 获取日期索引
    column_idx = your_data["header"].index("Confirmed")  # 获取标题的索引
    confirmed0124 = data[row_idx, column_idx]
    print("截止 2020-01-24 的累积数：", confirmed0124)

    row_idx = your_data["date"].index("2020-07-23")  # 获取日期索引
    column_idx = your_data["header"].index("New deaths")  # 获取标题的索引
    result = data[row_idx, column_idx]
    print("截止 2020-07-23 的数：", result)

    # 求和计算
    row1_idx = your_data["date"].index("2020-01-25")
    row2_idx = your_data["date"].index("2020-07-22")
    new_cases_idx = your_data["header"].index("New cases")

    # 注意要 row1_idx + 1 得到从 01-25 这一天的新增
    # row2_idx + 1 来包含 7 月 22 的结果
    new_cases = data[row1_idx + 1: row2_idx + 1, new_cases_idx]
    # print(new_cases)
    overall = new_cases.sum()
    print("总共：", overall)

    # 比例计算
    new_cases_idx = your_data["header"].index("New cases")
    new_recovered_idx = your_data["header"].index("New recovered")

    not_zero_mask = data[:, new_recovered_idx] != 0
    ratio = data[not_zero_mask, new_cases_idx] / data[not_zero_mask, new_recovered_idx]

    # 平均值, 标准差
    ratio_mean = ratio.mean()
    ratio_std = ratio.std()
    print("平均比例：", ratio_mean, "；标准差：", ratio_std)


if __name__ == '__main__':
    print_hi('数据分析')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
