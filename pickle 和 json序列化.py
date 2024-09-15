# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
import pickle
import os
import json


class File04:
    def __init__(self, name, create_time, size):
        self.name = name
        self.create_time = create_time
        self.size = size

    def change_name(self, new_name):
        self.name = new_name


class File03:
    def __init__(self, name, create_time, size):
        self.name = name
        self.create_time = create_time
        self.size = size
        self.file = open(name, "w")

    def __getstate__(self):
        # pickle 出去需要且能被 pickle 的信息
        pickled = {"name": self.name, "create_time": self.create_time, "size": self.size}
        return pickled

    def __setstate__(self, pickled_dict):
        # unpickle 加载回来，重组 class
        self.__init__(
            pickled_dict["name"], pickled_dict["create_time"], pickled_dict["size"])


class File02:
    def __init__(self, name, create_time, size):
        self.name = name
        self.create_time = create_time
        self.size = size
        self.file = open(name, "w")


class File:
    def __init__(self, name, create_time, size):
        self.name = name
        self.create_time = create_time
        self.size = size

    def change_name(self, new_name):
        self.name = new_name


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press ⌘F8 to toggle the breakpoint.
    # 主要涉及到的功能
    # Pickle
    # pickle.dumps()
    # pickle.dump()
    # pickle.load()
    # Json
    # json.dumps()
    # json.dump()
    # json.load()
    data = {"filename": "f1.txt", "create_time": "today", "size": 111}
    print(pickle.dumps(data))
    # 用 pickle.dump() 将字典直接转换成一个文件。
    data = {"filename": "f1.txt", "create_time": "today", "size": 111}
    with open("data.pkl", "wb") as f:
        pickle.dump(data, f)
    print(os.listdir())

    with open("data.pkl", "rb") as f:
        data = pickle.load(f)
    print(data)

    # 打包类，File类
    data = File("f2.txt", "now", 222)
    # 存
    with open("data.pkl", "wb") as f:
        pickle.dump(data, f)
    # 读
    with open("data.pkl", "rb") as f:
        read_data = pickle.load(f)
    print(read_data.name)
    print(read_data.size)

    # 依赖外部系统状态的对象不能被序列化，比如 打开的文件，网络连接，线程，进程，栈帧等等。
    # data = File02("f3.txt", "now", 222)
    # pickle 存，会报错
    # TypeError: cannot pickle '_io.TextIOWrapper' object
    # with open("data.pkl", "wb") as f:
    #     pickle.dump(data, f)

    # 硬要用依赖外部系统状态的对象去 pickle 保存，可以规避一下
    # pickle.dump() 会调用 __getstate__() 获取序列化的对象。 __setstate__() 在反序列化时被调用。

    data = File03("f3.txt", "now", 222)
    # 存
    with open("data.pkl", "wb") as f:
        pickle.dump(data, f)
    # 读
    with open("data.pkl", "rb") as f:
        read_data = pickle.load(f)
    print(read_data.name)
    print(read_data.size)
    print()

    # Json
    data = {"filename": "f1.txt", "create_time": "today", "size": 111}
    j = json.dumps(data)
    print(j)
    print(type(j))
    print()

    # Json 储存数据
    data = {"filename": "f1.txt", "create_time": "today", "size": 111}
    with open("data.json", "w") as f:
        json.dump(data, f)

    print("直接当纯文本读：")
    with open("data.json", "r") as f:
        print(f.read())

    print("用 json 加载了读：")
    with open("data.json", "r") as f:
        new_data = json.load(f)
    print("字典读取：", new_data["filename"])
    print()
    #  json 不能序列化保存 class
    # TypeError: Object of type File is not JSON serializable
    data = File04("f4.txt", "now", 222)
    # 存，会报错
    # with open("data.json", "w") as f:
    #     json.dump(data, f)

    # Pickle 和 Json 的不同
    # 存储格式  Python 特定的 Bytes 格式   通用 JSON text 格式，可用于常用的网络通讯中
    # 数据种类  类，功能，字典，列表，元组等  基本和 Pickle 一样，但不能存类，功能
    # 保存后可读性  不能直接阅读  能直接阅读
    # 跨语言性  只能用在 Python  可以跨多语言读写
    # 处理时间  长（需编码数据）  短（不需编码）
    # 安全性  不安全（除非你信任数据源） 相对安全


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('pickle 和 json 序列化')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
