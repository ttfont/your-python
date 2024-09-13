# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press ⌘F8 to toggle the breakpoint.


# 定义 class
class File:
    # __init__() 在类实例化时触发一次 __init__ 功能，它可以用来初始化配置
    def __init__(self):
        # self 获取这个类的自己的属性或功能时使用它
        self.name = "f1"
        self.create_time = "today"


# class 的功能
# 类似函数功能 可以给 __init__() 加上入参，在初始化时传入参数
class File01:
    def __init__(self, name, create_time="today"):
        self.name = name
        self.create_time = create_time

    # 一个类中可以定义多个方法
    def change_name(self, new_name):
        # 修改这个类中的属性，使用 self 调用 name 并修改属性
        self.name = new_name

    # 定义一个有返回的函数，在类中定义函数 需要加上 self
    def get_info(self):
        return self.name + " is created at " + self.create_time


# 继承
class Video:
    def __init__(self, name, window_size=(1080, 720)):
        self.name = name
        self.window_size = window_size
        self.create_time = "today"


class Text:
    def __init__(self, name, language="zh-cn"):
        self.name = name
        self.language = language
        self.create_time = "today"


# Video 和 Text 中有共同的属性，是不是可以减少共有属性/功能的重复开发——继承

# 继承示例
class File02:
    def __init__(self, name, create_time="today"):
        self.name = name
        self.create_time = create_time

    def get_info(self):
        return self.name + "is created at" + self.create_time


class Video02(File02):  # 继承了 File 的属性和功能
    def __init__(self, name, window_size=(1080, 720)):
        # 将共用属性的设置导入 File 父类
        super().__init__(name=name, create_time="today")
        self.window_size = window_size


class Text02(File02):  # 继承了 File 的属性和功能
    def __init__(self, name, language="zh-cn"):
        # 将共用属性的设置导入 File 父类
        super().__init__(name=name, create_time="today")
        self.language = language

    # 也可以在子类里复用父类功能
    def get_more_info(self):
        return self.get_info() + ", using language of " + self.language


# 私有属性和功能
class File03:
    def __init__(self):
        self.name = "f1"
        self.__deleted = False  # 我不让别人用这个变量
        self._type = "txt"  # 我不想别人使用这个变量

    def delete(self):
        self.__force_delete()

    # 私用变量无法访问，只能内部访问
    def __force_delete(self):  # 我不让别人使用这个功能
        self.__deleted = True
        return True

    # 不建议直接访问
    def _soft_delete(self):  # 我不想让别人使用这个功能
        return self.__force_delete()  # 我自己可以在内部随便调用

    # 可以这样访问
    def delete_self(self):
        return self._soft_delete()

    # 私有	特点
    # _ 一个下划线开头	弱隐藏 不想让别人用 （别人在必要情况下还是可以用的）
    # __ 两个下划线开头	强隐藏 不让别人用

    # 特殊方法，"__xx__" 前后双下划线，这种方法被称为魔术方法，一般是系统定义名字，类似于__init__()，一般是给Python调用的。
    # 定义	含义
    # def __init__()	初始化实例
    # def __repr__()	字符串的“官方”表现形式
    # def __str__()	字符串的“非正式”值
    # def __iter__()	遍历某个序列
    # def __next__()	从迭代器中获取下一个值

    # ”_“ 是私有的，一般不应该被调用
    # ”__“ 是为了避免子类重写某个函数而使用的
    # ”__xx__“ 一般是用于Python调用


class WrongMethod(object):
    def __init__(self, n):
        self.n = n

    # 重载加法运算符 (__add__ 方法) 它不执行标准的 Python 加法
    def __add__(self, other):
        return self.n - other

    # 重载减法运算符 (__sub__ 方法) 它不执行标准的 Python 减法
    def __sub__(self, other):
        return self.n + other

    def __str__(self):
        return str(self.n)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('Class 类')

    # See PyCharm help at https://www.jetbrains.com/help/pycharm/

    # 类的实例化和调用
    my_file = File()
    print(my_file.name)
    print(my_file.create_time)
    print()
    # 修改类的属性
    my_file.name = "new_name"
    print(my_file.name)
    print()
    # 在初始化时传入参数
    my_file01 = File01("my_file01")
    print(my_file01.name)
    print(my_file01.create_time)
    # 函数无参数返回时，会打印 None
    print(my_file01.change_name("new_name"))
    print(my_file01.name)
    print()
    print(my_file01.get_info())
    print()
    v02 = Video02("my_video")
    t02 = Text02("my_text")
    print(v02.get_info())  # 调用父类的功能
    print(t02.create_time)  # 调用父类的属性
    print(t02.language)  # 调用自己的属性
    print(t02.get_more_info())  # 调用自己加工父类的功能
    print()
    f03 = File03()
    print(f03._type)  # 可以拿到值，但是这个类的作者不想让你直接这样拿到
    print(f03._soft_delete())  # 可以调用，但是这个类的作者不想让你直接调用
    print(f03.delete_self())
    # 接下来的两个实验都会报错
    #  f03.__force_delete()
    num = WrongMethod(20)
    print("num = ", num)
    # 这里返回的答案时错误的，是重载之后重新定义的方法
    print("num + 10 = ", num + 10)
    # 这里返回的答案时错误的，是重载之后重新定义的方法
    print("num - 10 = ", num - 10)
    # - 在`__add__`方法中，实际执行的是减法操作。
    # - 在`__sub__`方法中，实际执行的是加法操作。
    # 这种实现虽然在功能上是有效的，但可能会引起阅读和使用代码的人的困惑，因为它违背了常规的期望和实践。通常，我们期望
    # `__add__`和`__sub__`分别实现标准的加法和减法行为。
