# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press ⌘F8 to toggle the breakpoint.
    # 为什么有生成器
    # 数据量大容易把内存撑爆
    items = []  # 假设这里在记录一个很大的列表
    for item in range(5):
        if item % 2 == 0:
            items.append(item)

    for i in items:
        print(i)
    # 生成器的 yield 方式重新定义
    for i in need_return():
        print("我在外面接到了一个 item=%d\n" % i)

    # 生成器也可以有复杂的逻辑 need_return02
    for i in need_return02():
        print(i)

    # 自定义生成器的初始化
    # 生成器是一个函数，可以传参控制初始化方式
    for i in need_return03(10):
        print(i)

    print()
    # 定义迭代器类，迭代器（iterator）和生成器（generator）都用于迭代操作。
    for i in NeedReturn(10):
        print(i)


def need_return():
    for item in range(5):
        if item % 2 == 0:
            print("我要扔出去一个 item=%d 了" % item)
            yield item  # 这里就会返回给下面的 for 循环
            print("我又回到里面了")


def need_return02():
    tmp = 2
    for item in range(300):
        if item == tmp:
            tmp *= item
            yield item


def need_return03(init_value):
    tmp = init_value
    for item in range(300):
        if item == tmp:
            tmp *= 2
            yield item


# 一个迭代器的写法，迭代器 要 __iter__ 和 __next__
class NeedReturn:
    def __init__(self, init_value=0):
        self.tmp = init_value
        self.item = 0

    def __iter__(self):
        return self

    def __next__(self):
        while True:
            if self.item == self.tmp:
                self.tmp *= 2
                return self.item
            self.item += 1
            if self.item == 300:
                raise StopIteration


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('为什么要有生成器')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
