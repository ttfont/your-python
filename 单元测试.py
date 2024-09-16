# This is a sample Python script.
import unittest


# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press ⌘F8 to toggle the breakpoint.

    # 什么是 Unittest

    # 不用 Unittest 单元测试，可能是先运行试试
    # ZeroDivisionError: division by zero
    # 这种方式比较适合
    # 小型项目，
    # 没有多少个功能的项目，
    # 而且项目功能之间并不会有任何联系。
    # my_div(1, 0)


def my_div(a, b):
    return a / b

    # 使用 unittest

    # TestFunc 继承 unittest.TestCase
    # class TestFunc(unittest.TestCase):
    #     def test_div(self):
    #         # 运行之后 OK
    #         self.assertEqual(2, my_div(2, 1))
    #         self.assertEqual(-2, my_div(2, -1))

    # class TestFunc02(unittest.TestCase):
    #     def test_div(self):
    #         # 这里后面我填了一个 1 纯粹是为了占一个位置，2/0 != 1，你知道的，
    #         # 后面我们再介绍更优雅的写法
    #         # 运行之后 FAILED (errors=1)
    #         self.assertEqual(1, my_div(2, 0))

    unittest.main()

    # unittest 规范
    # 假如要开发一个：输入 1 返回 2，输入 - 1 返回 3 ，输入其他任何数，返回 1 的程序
    # 建议先写 unittest 当中的 case，再写你要封装的函数 my_func03


def my_func03(a):
    # 逻辑先空在这里
    return None


# class TestFunc03(unittest.TestCase):
#     def test_func(self):
#         self.assertEqual(2, my_func03(1))
#         self.assertEqual(3, my_func03(-1))
#         for i in range(-100, 100):
#             if i == 1 or i == -1:
#                 continue
#             self.assertEqual(1, my_func03(i))
# 建议一个 py 文件一个 test ，比如文件是 yourpython.py ,则单元测试可以命名为 yourpython_test.py


# 有时候要测试多个功能
def my_func1(a):
    if a == 1:
        return 2
    elif a == -1:
        return 3
    else:
        return 1


def my_func2(b):
    if b != "yes":
        raise ValueError("you can only say yes!")
    else:
        return True


class TestFunc04(unittest.TestCase):
    def test_func1(self):
        self.assertEqual(2, my_func1(1))
        self.assertEqual(3, my_func1(-1))
        for i in range(-100, 100):
            if i == 1 or i == -1:
                continue
            self.assertEqual(1, my_func1(i))

    def test_func2(self):
        self.assertTrue(my_func2("yes"))
        with self.assertRaises(ValueError):
            my_func2("nononono")

    # 用 Python 命令执行测试
    # python -m unittest 单元测试.py

    # 能测哪些 assert，在 unittest 的模块中有特别丰富的测试方式，常用的方法
    # 。。。


# 想测单独的功能
# 第一种，使用 TestSuite() 和 TextTestRunner()
class TestFunc05(unittest.TestCase):
    def test_func1(self):
        self.assertEqual(2, my_func1(1))
        self.assertEqual(3, my_func1(-1))
        for i in range(-100, 100):
            if i == 1 or i == -1:
                continue
            self.assertEqual(1, my_func1(i))

    def test_func2(self):
        self.assertTrue(my_func2("yes"))
        with self.assertRaises(ValueError):
            my_func2("nononono")


# 定义一个 suite 替换 unittest.main()
suite = unittest.TestSuite()
suite.addTest(TestFunc04('test_func1'))
unittest.TextTestRunner().run(suite)

# 第二种，Python 的命令来执行不同的 test
# python -m unittest 单元测试.TestFunc05.test_func2
# python -m unittest 单元测试.TestFunc05.test_func1

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('单元测试')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
