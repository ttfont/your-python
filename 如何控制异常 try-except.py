# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press ⌘F8 to toggle the breakpoint.

    # 一些可遇见的报错，没有文件时报错
    # FileNotFoundError: [Errno 2] No such file or directory: 'no_file.txt'
    # with open("no_file.txt", "r") as f:
    #     print(f.read())

    # 处理的异常类型 FileNotFoundError
    try:
        with open("no_file.txt", "r") as f:
            print(f.read())
    except FileNotFoundError as e:
        # 打印出异常
        print(e)
        with open("no_file.txt", "w") as f:
            f.write("I'm no_file.txt")
        print("new file 'no_file.txt' has been written")
    #  一些可遇见的异常 FileNotFoundError 异常已经被 except 给捕捉了，
    # 捕捉了之后 处理 except 的下一段逻辑

    # 处理多个异常
    d = {"name": "f1", "age": 2}
    l = [1, 2, 3]
    try:
        # key or index error for: 'gender'
        v = d["gender"]
        # key or index error for: list assignment index out of range
        l[3] = 4
    except (KeyError, IndexError) as e:
        print("key or index error for:", e)

    # 分开处理异常，程序顺序执行的时候，只要是报错了， 它终止错误之后的代码，进入到错误处理阶段
    d = {"name": "f1", "age": 2}
    l = [1, 2, 3]
    try:
        v = d["gender"]
        l[3] = 4
    except KeyError as e:
        print("key error for:", e)
        d["gender"] = "x"
    except IndexError as e:
        print("index error for:", e)
        l.append(4)
    print(d)
    print(l)

    # try-except-else，这个模式，在 else 中处理没有报错的情况
    l = [1, 2, 3]
    try:
        # list assignment index out of range
        l[3] = 4
    except IndexError as e:
        print(e)
    else:
        print("报错了 no error, now in else")
    # 不报错执行 else 中的逻辑
    l = [1, 2, 3, 4]
    try:
        l[3] = 4
    except IndexError as e:
        print(e)
    else:
        print("没报错 no error, now in else")

    # try-except-finally 不管有没有异常 finally 都执行
    # 异常
    l = [1, 2, 3]
    try:
        # list assignment index out of range
        l[3] = 4
    except IndexError as e:
        print(e)
    finally:
        print("reach finally 异常")
    # 正常
    l = [1, 2, 3, 4]
    try:
        l[3] = 4
    except IndexError as e:
        print(e)
    finally:
        print("reach finally 正常")

    # 不处理异常，finally 都执行
    # try:
    #     # NameError: name 'dddddd' is not defined
    #     dddd = dddddd
    # finally:
    #     print("I know there is error, so what ?  dddd = dddddd")

    # raise 手动触发异常，提示调用此函数时抛错的原因，这是一个很友善的操作
    # print(no_negative(-1))

    # Python异常错误名称表
    # 能被 raise 的 error

    # 异常名称	描述
    # BaseException	所有异常的基类
    # SystemExit	解释器请求退出
    # KeyboardInterrupt	用户中断执行(通常是输入^C)
    # Exception	常规错误的基类
    # StopIteration	迭代器没有更多的值
    # GeneratorExit	生成器(generator)发生异常来通知退出
    # StandardError	所有的内建标准异常的基类
    # ArithmeticError	所有数值计算错误的基类
    # FloatingPointError	浮点计算错误
    # OverflowError	数值运算超出最大限制
    # ZeroDivisionError	除(或取模)零 (所有数据类型)
    # AssertionError	断言语句失败
    # AttributeError	对象没有这个属性
    # EOFError	没有内建输入,到达EOF 标记
    # EnvironmentError	操作系统错误的基类
    # IOError	输入/输出操作失败
    # OSError	操作系统错误
    # WindowsError	系统调用失败
    # ImportError	导入模块/对象失败
    # LookupError	无效数据查询的基类
    # IndexError	序列中没有此索引(index)
    # KeyError	映射中没有这个键
    # MemoryError	内存溢出错误(对于Python 解释器不是致命的)
    # NameError	未声明/初始化对象 (没有属性)
    # UnboundLocalError	访问未初始化的本地变量
    # ReferenceError	弱引用(Weak reference)试图访问已经垃圾回收了的对象
    # RuntimeError	一般的运行时错误
    # NotImplementedError	尚未实现的方法
    # SyntaxError	Python 语法错误
    # IndentationError	缩进错误
    # TabError	Tab 和空格混用
    # SystemError	一般的解释器系统错误
    # TypeError	对类型无效的操作
    # ValueError	传入无效的参数
    # UnicodeError	Unicode 相关的错误
    # UnicodeDecodeError	Unicode 解码时的错误
    # UnicodeEncodeError	Unicode 编码时错误
    # UnicodeTranslateError	Unicode 转换时错误
    # Warning	警告的基类
    # DeprecationWarning	关于被弃用的特征的警告
    # FutureWarning	关于构造将来语义会有改变的警告
    # OverflowWarning	旧的关于自动提升为长整型(long)的警告
    # PendingDeprecationWarning	关于特性将会被废弃的警告
    # RuntimeWarning	可疑的运行时行为(runtime behavior)的警告
    # SyntaxWarning	可疑的语法的警告
    # UserWarning	用户代码生成的警告


def no_negative(num):
    if num < 0:
        raise ValueError("I said no negative")
    return num


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('如何控制异常 try-except')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
