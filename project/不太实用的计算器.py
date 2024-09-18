# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press ⌘F8 to toggle the breakpoint.
    # 项目实践 不太实用的计算器
    # 做个小项目，把前面学到的知识用起来
    # 发现问题、分析问题、解决问题、总结复盘
    # 预备课:
    # class类
    # 变量与运算的数学运算
    # 数据种类
    # for 和 while 循环

    # 假如现在你手上没有计算器，需要设计一个计算器（发现问题）

    # 产品定位
    # 计算两个数的加减乘除等一些常用方法
    # 一次性计算一批数据的运算结果

    # 程序设计
    # 程序设计出来要批量化生成，需要把封装在一起，标准化，然后批量生产出来，这个需要前面学到的知识 class类


# 变量与运算的数学运算
class Calculator:
    def add(self, a, b):
        return a + b

    def subtract(self, a, b):
        return a - b

    def multiply(self, a, b):
        return a * b

    def divide(self, a, b):
        # 这里我们得处理一个异常
        if b == 0:
            print("b cannot be 0")
        else:
            return a / b

# 使用计算器
c = Calculator()
print(c.add(1, 2))
print(c.divide(1, 2))
c.divide(1, 0)


# 批量计算：数据种类，for 和 while 循环，和继承
class Calculator01(Calculator):
    def subtract(self, a, b):
        return super().subtract(a, b)

    def batch_subtract(self, a_list, b_list):
        res_list = []
        for i in range(len(a_list)):
            res_list.append(self.subtract(a_list[i], b_list[i]))
        return res_list


c01 = Calculator01()
print(c01.subtract(2, 1))
# 批量计算 [3, 2, 1] 和 [3, 2, 1] 的差
print(c01.batch_subtract([3, 2, 1], [2, 3, 4]))


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('不太实用的计算器')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
