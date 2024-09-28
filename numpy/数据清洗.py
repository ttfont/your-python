# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
import numpy as np


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press ⌘F8 to toggle the breakpoint.
    raw_data = [
        ["Name", "StudentID", "Age", "AttendClass", "Score"],
        ["小明", 20131, 10, 1, 67],
        ["小花", 20132, 11, 1, 88],
        ["小菜", 20133, None, 1, "98"],
        ["小七", 20134, 8, 1, 110],
        ["花菜", 20134, 98, 0, None],
        ["刘欣", 20136, 12, 0, 12]
    ]
    # print(raw_data)

    data = np.array(raw_data)
    print("data.dtype", data.dtype)
    test1 = np.array([1, 2, 3])
    test2 = np.array([1.1, 2.3, 3.4])
    test3 = np.array([1, 2, 3], dtype=np.float64)
    print("test1.dtype", test1.dtype)
    print("test2.dtype", test2.dtype)
    print("test3.dtype", test3.dtype)
    print("test2 > 2 ", test2 > 2)
    # TypeError: '>' not supported between instances of 'str' and 'int'
    # print("data > 2", data > 2)  # 这里会报错
    # 数据预处理
    data_process = []
    for i in range(len(raw_data)):
        if i == 0:
            continue  # 不要首行字符串
        # 去掉首列名字
        data_process.append(raw_data[i][1:])
    data = np.array(data_process, dtype=np.float64)
    print("data.dtype", data.dtype)
    # print(data)
    # 清洗数据
    # 查看第一列学号
    sid = data[:, 0]
    unique, counts = np.unique(sid, return_counts=True)
    print(counts)
    # 数据中少 20135
    print(unique[counts > 1])
    # 修改第五行第一列
    data[4, 0] = 20135
    # print(data)
    # 查看第二列年龄
    is_nan = np.isnan(data[:, 1])
    print("is_nan:", is_nan)
    nan_idx = np.argwhere(is_nan)
    print(nan_idx)
    # 用 ~ 符号可以 True/False 对调
    print(~np.isnan(data[:, 1]))
    # 计算有数据的平均年龄，用 ~ 符号可以 True/False 对调
    print(data[~np.isnan(data[:, 1]), 1])
    mean_age = data[~np.isnan(data[:, 1]), 1].mean()
    print("有数据的平均年龄：", mean_age)
    # 发现平均均值偏高，查看数据发现有个年龄为 98 的，判断这个是异常数据
    # ~ 表示 True/False 对调，& 就是逐个做 Python and 的运算
    normal_age_mask = ~np.isnan(data[:, 1]) & (data[:, 1] < 20)
    print("normal_age_mask:", normal_age_mask)

    normal_age_mean = data[normal_age_mask, 1].mean()
    print("normal_age_mean:", normal_age_mean)

    data[~normal_age_mask, 1] = normal_age_mean
    print("ages:", data[:, 1])

    # 观察后面两数据
    print(data[-3:, 2:])
    # 因为没上课，就没成绩，但是倒数第一行，没上课，怎么还有成绩？还有倒数第三行，成绩居然超出了满分 100 分
    # 没上课的转成分数转成 0
    data[data[:, 2] == 0, 3] = 0

    # 超过 100 分和低于 0 分的都处理一下
    data[:, 3] = np.clip(data[:, 3], 0, 100)

    print(data[:, 2:])


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('数据清洗')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
