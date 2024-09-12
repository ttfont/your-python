# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press ⌘F8 to toggle the breakpoint.
    # List 列表
    files = ["f1.txt", "f2.txt", "f3.txt", "f4.txt", "f5.txt"]
    print("files[0] ", files[0])
    print("files[3] ", files[3])
    print("files[-1] ", files[-1])
    print("files[-3] ", files[-3])
    print()
    # 获取多个数据
    print("files[:3] ", files[:3])
    print("files[2:4] ", files[2:4])
    print("files[-3:] ", files[-3:])
    print()
    # 修改对应位置的数据
    print("old files[1] ", files[1])
    files[1] = 12
    print("new files[1] ", files[1])
    print()
    # 在列表中，你可以存放不同类型的元素，字符，数字，甚至列表里还能有列表。
    l = [1, "file", ["2", 3.2]]
    print(l)
    l[2][0] = "new string"
    print(l)
    print()

    # Dict 字典，在字典中的元素不像列表，字典元素是没有顺序的
    files = {"ID": 111, "passport": "my passport", "books": [1, 2, 3]}
    print(files)
    print(files["books"])
    print()
    files["ID"] = 222
    print(files)
    files["ID"] = [2, 3, 4]
    print(files)
    print()
    # Tuple 元组，元组里的数据不可变
    files = ("file1", "file2", "file3")
    print(files[1])
    print()
    # files[1] = "file4"  # 这里会报错

    # Set 集合，常用它去去重，在集合中的元素，其实是没有顺序的,集合可以用 ([])，也可以用 {}
    my_files = set(["file1", "file2", "file3"])
    print("my_files", my_files)
    your_files = {"file1", "file3", "file5"}
    print("your_files", your_files)
    print("交集 ", your_files.intersection(my_files))
    print("并集 ", your_files.union(my_files))
    print("补集 ", your_files.difference(my_files))
    print()
    # 列表在循环中运用
    files = ["f1.txt", "f2.txt", "f3.txt", "f4.txt", "f5.txt"]
    for i in range(len(files)):
        if files[i] == "f3.txt":
            print("I got f3.txt")
    print()
    # 字典在循环中运用
    files = {"ID": 111, "passport": "my passport", "books": [1, 2, 3]}
    for key in files.keys():
        print("key:", key)

    for value in files.values():
        print("value:", value)

    for key, value in files.items():
        print("key:", key, ", value:", value)
    print()
    # 其他功能
    files = []
    for i in range(5):
        files.append("f" + str(i) + ".txt")  # 添加
        print("has", files)

    for i in range(len(files)):
        print("pop", files.pop())  # 从最后一个开始 pop 出。取出之后当前数据被删除
        print("remain", files)

    files = ["f1.txt", "f2.txt"]

    # 其他功能list
    # 扩充入另一个列表
    files.extend(["f3.txt", "f4.txt"])
    print("extend", files)

    # 按位置添加
    files.insert(1, "file5.txt")  # 添加入第1位（首位是0哦）
    print("insert", files)

    # 移除某索引
    del files[1]
    print("del", files)

    # 移除某值
    files.remove("f3.txt")
    print("remove", files)

    # 其他功能字典
    files = {"ID": 111, "passport": "my passport", "books": [1, 2, 3]}

    # 按key拿取，并在拿取失败的时候给一个设定好的默认值
    print('files["ID"]:', files["ID"])
    print('files.get("ID"):', files.get("unknown ID", "不存在这个 ID"))

    # 将另一个字典补充到当前字典
    files.update({"files": ["1", "2"]})
    print('update:', files)

    # pop 调一个item，和列表的 pop 类似
    popped = files.pop("ID")
    print('popped:', popped)
    print("remain:", files)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('数据种类')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
