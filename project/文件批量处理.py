# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
import os
import re


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press ⌘F8 to toggle the breakpoint.
    # 项目实践 文件批量处理
    # 预备课：
    # 文件目录管理
    # for 和 while 循环
    # 读写文件
    # 正则表达式

    # 主要涉及功能
    # 找到所有文件
    # os.listdir()
    # os.path.join()
    # 找到文件特定字段
    # re.findall()
    # os.path.join()
    # 替换
    # os.path.join()
    # re.sub()
    # string.startswith()

    # 我遇到的问题 ，我们要处理大量文件 比如 1000 个文件，需要替换其中的特定字符，
    # 比如把 yourpython.github.io 改成 mofanpy.com

    # 分析问题
    # 遍历所有的文本文件
    # 找到文件中特定字段
    # 替换掉这个特定字段

    # 找到所有文件，文件目录管理
    print(os.listdir("yourfiles"))

    # 找到文件特定字段,for 和 while 循环,读写文件
    for filename in os.listdir("yourfiles"):
        file_path = os.path.join("yourfiles", filename)
        with open(file_path, "r") as f:
            print(file_path, ": ", f.read())

    # 找出复杂的字符串，正则表达式
    string = "这是我的主页 https://mofanpy.com, 这个 www.mofanpy.com 有很多 mofan 教你机器学习和 python 语言的教学"
    res = re.findall(r"(https://)?(mofanpy.com)", string)
    for r in res:
        print(r[1])

    # 替换，有二种方案
    # 在原文本上替换，并覆盖原文本的内容；
    # 复制出一个新的文件，将原文本替换过的文字拷贝到新文件中，原文件不改变。
    # 这里选择方案二
    for filename in os.listdir("yourfiles"):
        file_path = os.path.join("yourfiles", filename)
        with open(file_path, "r") as f1:
            string = f1.read()
            new_string = re.sub(r"yourpython.github.io", "mofanpy.com", string)
            with open(os.path.join("yourfiles", "new_" + filename), "w") as f2:
                f2.write(new_string)

    # 查看文件是否正确
    print()
    for filename in os.listdir("yourfiles"):
        if filename.startswith("new_"):
            continue
        file_path = os.path.join("yourfiles", "new_" + filename)
        with open(file_path, "r") as f:
            print(file_path, ": ", f.read())


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('文件批量处理')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
