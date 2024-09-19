# This is a sample Python script.
from typing import Callable, Any


# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press ⌘F8 to toggle the breakpoint.

    # Lambda: 更直接的 Function
    # 常规函数写法和调用
    print(add(1, 2))

    # 你发现你的情况是：
    # 我的功能很简单
    # 调用次数不多（没那么正式的功能）
    # lambda 写法，不是正式功能，你要临时使用的时候可以用。
    add01 = lambda a, b: a + b
    print(add01(1, 2))

    # 一行for能解决的事，干嘛写那么多
    # 有时候：
    #
    # 我想要出一个列表，
    # 然后用 for 循环不断添加列表里的元素。
    # 常规写法
    l01 = []
    for i in range(10):
        l01.append(i * 2)
    print(l01)
    # 可以这样写 ，比较简单的运算逻辑可以这样写
    l02 = [i * 2 for i in range(10)]
    print(l02)
    # 可以创建字典 ，比较简单的运算逻辑可以这样写
    d = {"index" + str(i): i * 2 for i in range(10)}
    print(d)
    # 可以一行判断，何必多行
    # 常规写法
    done = False
    if done:
        a = 1
    else:
        a = 2
    print(a)
    # 简写 ，比较简单的运算逻辑可以这样写
    done = False
    a = 1 if done else 2
    print(a)

    # 一行for+判断也行
    # 常规写法
    l = []
    for i in range(10):
        if i % 2 == 0:
            l.append(i * 2)
    print(l)
    # 简写
    # List
    l = [i * 2 for i in range(10) if i % 2 == 0]
    print(l)
    # dict
    d = {"index" + str(i): i * 2 for i in range(10) if i % 2 == 0}
    print(d)

    # enumerate 自动加 index
    # 常规的计数写法
    count = 0
    l = [11, 22, 33, 44]
    for data in l:
        if count == 2:
            data += 11
        l[count] = data
        # print(count)
        count += 1
    print(l, count)
    # 使用 enumerate, 这里的 count01 记录的是索引
    l = [11, 22, 33, 44]
    for count01, data in enumerate(l):
        if count01 == 2:
            data += 11
        l[count01] = data
        # print(count01)
    print(l, count01)
    print()
    l = [11, 22, 33, 44]
    d = {}
    # count 从 5 开始
    for count, data in enumerate(l, start=5):
        d[count] = data
        # print(count)
    print(d)
    # Zip让你同时迭代
    # 同时处理两个列表，一个是姓名一个是分数，并把它们做成一个字典
    name = ["a", "b", "c"]
    score = [1, 2, 3]
    d = {}
    for i in range(3):
        d[name[i]] = score[i]
    print(d)
    print()
    name = ["a", "b", "c"]
    score = [1, 2, 3]
    d = {}
    for n, s in zip(name, score):
        d[n] = s
    print(d)
    print()
    # 数据多一点
    name = ["a", "b", "c"]
    score = [1, 2, 3]
    bonus = [1, 0, 1]
    d = {}
    for n, s, b in zip(name, score, bonus):
        d[n] = s + b
    print(d)

    # reverse & reversed 逆转列表
    # 常规写法
    l = [1, 2, 3]
    _l = []
    for i in range(len(l)):
        _l.append(l[-i - 1])
    print(_l)
    # 简写
    l = [1, 2, 3]
    _l = [l[-i - 1] for i in range(len(l))]
    print(_l)
    # 语法糖 1
    l = [1, 2, 3]
    l.reverse()
    print(l)
    # 语法糖 2
    l = [1, 2, 3]
    for i in reversed(l):
        print(i)
    # 语法糖 3
    l = [1, 2, 3]
    _l = l[::-1]
    print(l)
    print(_l)


def add(a, b):
    return a + b


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('Python的偷懒用法')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
