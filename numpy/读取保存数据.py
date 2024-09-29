# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
import os
import numpy as np


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press ⌘F8 to toggle the breakpoint.
    # 加载常用数据格式
    # 常规方法读 os

    print("data file in directory:", os.listdir("csv"))
    with open("csv/data.csv", "r") as f:
        print("\n", f.read())
    # 使用 numpy 读
    data = np.loadtxt("csv/data.csv", delimiter=",", skiprows=1, dtype=np.int64)
    print(data)

    # 读字符串
    row_string = "20131, 10, 67, 20132, 11, 88, 20133, 12, 98, 20134, 8, 100, 20135, 9, 75, 20136, 12, 78"
    data = np.fromstring(row_string, dtype=np.int64, sep=",")
    data = data.reshape(6, 3)
    print("data ", data)

    # 保存数据
    # 保存为文本格式
    print("numpy data:\n", data)
    np.savetxt("csv/save_data.csv", data, delimiter=",", fmt='%s')

    print("data file in directory:", os.listdir("csv"))
    with open("csv/save_data.csv", "r") as f:
        print("\n", f.read())
    # 保存二进制文件
    # np.save()
    # 来保存，保存的是一个以.npy
    # 结尾的二进制文件。加载的时候，我们能用
    # np.load()
    # 直接加载这个二进制数据文件。
    np.save("csv/save_data_10.npy", data)

    print("data file in directory:", os.listdir("csv"))
    npy_data = np.load("csv/save_data_10.npy")
    print(npy_data)
    # 分开多个 array 来存放，一个 numpy 文件中保存多个 numpy array
    train_data = np.array([1, 2, 3])
    test_data = np.array([11, 22, 33])

    np.savez("csv/save_data_02.npz", train=train_data, test=test_data)
    print("data file in directory:", os.listdir("csv"))

    npz_data = np.load("csv/save_data_02.npz")
    print("train:", npz_data["train"])
    print("test:", npz_data["test"])
    # np.savez_compressed() 数据压缩
    print()
    np.savez_compressed("csv/save_data_compressed.npz", train=train_data, test=test_data)
    print("data file in directory:", os.listdir("csv"))

    npz_data_compressed = np.load("csv/save_data_compressed.npz")
    print("train:", npz_data_compressed["train"])
    print("test:", npz_data_compressed["test"])

    print("compressed file size:", os.path.getsize("csv/save_data_compressed.npz"))
    print("original file size:", os.path.getsize("csv/save_data_02.npz"))


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('读取保存数据')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
