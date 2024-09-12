# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press ⌘F8 to toggle the breakpoint.
    # 定义函数
    # 未定义多个文件名进行一种规则性修改
    f1 = "f1"
    f2 = "f2"

    f1 += ".txt"
    f1 = "my_" + f1
    f2 += ".txt"
    f2 = "my_" + f2
    print(f1, f2)
    print()


# 定义函数将重复的工作逻辑集合起来，含输入参数
def modify_name(filename):
    filename += ".txt"
    filename = "my_" + filename
    print(filename)


# 不含输入参数
def my_func():
    filename = "不含输入参数f1"
    ext = ".txt"
    total_name = filename + ext
    print(total_name)


# 拿出函数处理的结果（有返回参数）
def modify_name(filename):
    filename += ".txt"
    filename = "my_" + filename
    return filename


# 参数设置
def f(x, a, b, c):
    return a * x ** 2 + b * x + c * 1


# 参数设置默认值, 调用函数的时候就不一定要给这个参数赋值，不赋值去默认值
def f(x, a=1, b=1, c=0):
    return a * x ** 2 + b * x + c * 1


# 全局和局部变量
# 变量	特点
# 全局 global	函数里外都能用 （公用）
# 局部 local	仅在函数内有用 （私有）
def modify_name01():
    filename = "f1.txt"
    print("local filename:", filename)


filename01 = "f1.txt"


def modify_name02():
    print("在函数里调用全局变量 local filename:", filename01)


filename03 = "f1.txt"


def modify_name03():
    # 在函数里修改全局变量
    filename03 = "f2.txt"
    # 在本函数生效
    print("函数里面 local filename:", filename03)


filename04 = "filename1.txt"


def modify_name04():
    # 必须要修改全局变量 则在变量前加 global 关键字
    global filename04  # 提出申请
    filename04 = "filename2GLO.txt"
    print("修改全局变量 里面 local filename:", filename04)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('Function 函数')
    # See PyCharm help at https://www.jetbrains.com/help/pycharm/
    # 调用函数
    modify_name("F1")
    modify_name("F2")
    # 不含输入参数
    my_func()
    print()
    new_filename = modify_name("有返回结果f1")
    print(new_filename)
    print()
    # 忽略参数名，按顺序传参
    print("忽略参数名，按顺序传参 = ", f(2, 1, 1, 0))
    # 写上参数名，按名字传参
    print("写上参数名，按名字传参 = ", f(x=2, a=1, b=1, c=0))
    # 若用参数名，可以打乱顺序传参
    print("若用参数名，可以打乱顺序传参 = ", f(a=1, c=0, x=2, b=1))
    print()
    print("有默认值的调用 a = ", f(2, a=2))
    print("有默认值的调用 b = ", f(2))

    modify_name01()
    # 这里会报错。这里不能调用 modify_name01 中的局部变量否则报错
    # print("global filename:", filename)

    modify_name02()
    # 调用共有变量
    print("global filename:", filename01)
    print()
    modify_name03()
    # 函数外面的全局变量值未改变
    print("函数外面 global filename:", filename03)
    print()
    # 修改全局变量
    modify_name04()
    # 增加 global 关键字后，从结果来看修改成功了
    print("修改全局变量 外面 global filename:", filename04)
