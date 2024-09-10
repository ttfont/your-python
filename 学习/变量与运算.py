# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press ⌘F8 to toggle the breakpoint.
    # 英文的单引号
    v1 = '文件管理系统v1'
    # 英文的双引号
    v2 = "文件管理系统v2"
    # 三个引号（可单/双引）
    v3 = """文件管理系统v3"""
    v4 = '''文件管理系统v4'''
    print("v1 = " + v1)
    print("v2 = " + v2)
    print("v3 = " + v3)
    print("v4 = " + v4)

    # 三个引号可以书写跨行
    v5 = '''床前明月光，疑是地上霜。
     举头望明月，低头思故乡。'''
    print("v5 = " + v5)
    # 多个变量
    n1, n2, n3 = "文件", "系统", "管理"
    print(n1, n2, n3)
    # 多个变量赋予相同的值
    m4 = m5 = m6 = "文件系统"
    print(m4, m5, m6)
    # print 一次性打出很多不同的变量内容
    print("多个不同的变量 ", n1, n2, n3)

    # 常规的数学运算
    num_of_files = 10
    print("我系统里有", num_of_files, "个文件")
    print("分五组，每组", num_of_files / 5, "个")

    # 运算符	描述	例子
    # +	加	3+4=7
    # -	减	3-4=-1
    # *	乘	3*4=12
    # /	除	3/2=1.5
    # %	取模	103%100=3
    # **	幂	3**2=9
    # //	取整除	10//3=3

    # 字符串也可以拼接
    str = "文件" + "系统"
    print(str)

    # 运算方法简写
    a = 1
    a += 1
    print("a += ", a)
    a -= 1
    print("a -= ", a)
    a *= 10
    print("a *= ", a)
    a /= 2
    print("a /= ", a)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('变量与运算')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
