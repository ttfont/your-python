# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press ⌘F8 to toggle the breakpoint.
    # 为 Function 做额外的事
    # 在一个 Function 中调用另一个 Function 做处理

    outer_fn("mofanpy")

    # 有时候做前处理和后处理，需要定义两个 inner function
    outer_fn02("mofanpy")

    # Decorator 装饰器在做前后处理时非常有用
    # 比如鉴权 验证数据有效性 后置处理数据
    # 定义一个装饰器 Decorator Function
    # 先用一个没有装饰器， function 是可以被当做参数传入另一个 function
    decorator(outer_fn03, "mofanpy 了 ")
    # 定义一个装饰器 Decorator Function
    outer_fn04("mofanpy")
    # 定义一个装饰器 Decorator 作前处理后处理
    outer_fn05("mofanpy")
    # 定义一个鉴权
    outer1("mofanpy outer1 ")
    outer2("mofanpy")
    outer3("mofanpy outer3")


def authorization(fn):
    def check_and_do(name):
        if name != "mofanpy":  # 鉴权
            print(name + " has no right!")
            return
        res = fn(name)
        return res

    return check_and_do


@authorization
def outer1(name):
    print(name + " outer1")


@authorization
def outer2(name):
    print(name + " outer2")


@authorization
def outer3(name):
    print(name + " outer3")


def decorator03(fn):
    def wrapper(name):
        print(name + "say I'm in_pre")  # 这是我的前处理
        res = fn(name)
        print(name + "say I'm in_post")  # 这是我的后处理
        return res

    return wrapper


@decorator03
def outer_fn05(name):
    print(name + "say I'm out")


# 定义一个装饰器 Decorator
def decorator02(fn):
    def wrapper(name):
        print(name + "say I'm in，decorator02")  # 这是我的前处理
        return fn(name)

    return wrapper


@decorator02
def outer_fn04(name):
    print(name + "say I'm out，outer_fn04")


# 先用一个没有装饰器 start
def decorator(fn, name):
    print(name + "say I'm in")  # 这是我的前处理
    return fn(name)


def outer_fn03(name):
    print(name + "say I'm out，outer_fn03")


# 先用一个没有装饰器 end

def inner_fn(name):
    print(name + "say I'm in")


# 在一个 Function 中调用另一个 Function
def outer_fn(name):
    inner_fn(name)
    print(name + "say I'm out")


# 有时候做前处理和后处理，需要定义两个 inner function
def inner_pre_fn(name):
    print(name + "say I'm in_pre")


def inner_post_fn(name):
    print(name + "say I'm in_post")


def outer_fn02(name):
    inner_pre_fn(name)
    print(name + "say I'm out")
    inner_post_fn(name)


#

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('套娃的装饰器')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
