# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press ⌘F8 to toggle the breakpoint.

    # if 如果
    in_trash = True
    if in_trash:
        print("可以被彻底删除")

    in_trash = True
    if not in_trash:
        print("不可以被彻底删除")

    # if-else 如果否则
    in_trash = True
    if in_trash:
        print("可以被彻底删除")
    else:
        print("不可以被彻底删除")

    # 判断条件

    # 判断	含义
    # a == b	a 是否等于 b
    # a > b	a 是否大于 b
    # a >= b	a 是否大于等于 b
    # a < b	a 是否小于 b
    # a <= b	a 是否小于等于 b
    # a != b	a 是否不等于 b
    # 文字之间的判断
    a, b = "文件1", "文件2"
    print(a == b)
    print("2 < 3", 2 < 3)
    print("3 < 2", 3 < 2)
    print("2 != 2", 2 != 2)

    print(2 < 3 and 2 < 5)
    print(2 > 3 or 3 == 3)
    print(2 > 3 or not 3 == 3 and 5 < 10)
    # and or not 的含义
    #True and True 需要两边同时满足才能返回 True
    #True or False 只要一边是 True 则返回 True
    #not True 给出相反结果

    a, b = 1, 2
    if a > b:
        print("a 大于 b")
    else:
        print("a 不大于 b")

    # if -elif - else
    today = 4
    if today == 1:
        print("周一")
    elif today == 2:
        print("周二")
    elif today == 3:
        print("周三")
    else:
        print("周一周二周三之外的一天")

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('条件判断')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
