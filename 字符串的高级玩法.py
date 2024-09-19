# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press ⌘F8 to toggle the breakpoint.

    # %百分号模式
    name = "Your Python"
    print("我的名字是 " + name + "！")
    print("我的名字是 %s!" % name)

    # 多参数时字符串的传入
    name01 = "Your Python"
    age = 18
    gender = "男"
    print("我的名字是 " + name01 + "！我" + str(age) + "岁了，我是" + gender + "的~")
    print("我的名字是 %s !我 %d 岁了，我是 %s 的~" % (name01, age, gender))

    # 用字典的形式录入，不用关心参数的顺序，字典的key对应上就可以
    name02 = "Your Python"
    age02 = 18
    gender02 = "男"
    print("我的名字是 %(nm)s !我 %(age)d 岁了，我是 %(gd)s 的~" % {"nm": name02, "age": age02, "gd": gender02})

    # 注意一些 % 后面参数的意思
    name03 = "Your Python"
    age03 = 18
    height03 = 1.8
    print(" 我的名字是 %s !我 %d 岁了，我 %f 米高~" % (name03, age03, height03))

    # 控制小数的长度
    print("%f" % (1 / 3))
    print("%.2f" % (1 / 3))

    print("%f" % (1 / 3))  # 后面不限制
    print("%.2f" % (1 / 3))  # 后面限制 2 个位置
    print("%4d" % (1 / 3))  # 前面补全最大 4 个位置 （包含本身数字的占位）
    print("%5d" % 12)  # 前面补全最大 5 个位置（包含本身数字的占位）

    # format功能更多，format 不需要关注数据类型。使用 {} 占位
    name04 = "Your Python"
    age04 = 18
    height04 = 1.8
    print("我的名字是 %s !我 %d 岁了，我 %f 米高~" % (name04, age04, height04))
    print("我的名字是 {} !我 {} 岁了，我 {} 米高~".format(name04, age04, height04))

    # {0} 中的数字代表 format 里的数据索引，索引是从 0 开始的。这样就可以多次复用 format 里的数据。
    name05 = "Your Python"
    age05 = 18
    height05 = 1.8
    print("我的名字是 {0} !我 {1} 岁了，我 {2} 米高~我是{0}".format(name05, age05, height05))

    # 字典模式
    name06 = "Your Python"
    age06 = 18
    height06 = 1.8
    print("我的名字是 {nm} !我 {age} 岁了，我 {ht} 米高~我是{nm}".format(nm=name06, age=age06, ht=height06))

    # 格式化数据
    print("我 {:.3f} 米高".format(1.12345))
    print("我 {ht:.1f} 米高".format(ht=1.12345))
    print("我 {:3d} 米高".format(1))  # 前面补全最大 3 个位置
    print("我 {:3d} 米高".format(21))  # 前面补全最大 3 个位置

    # 乘以 100%
    txt = "You scored {:%}"
    print(txt.format(2.1234))

    # 乘以 100% 保留两位小数
    txt = "You scored {:.2%}"
    print(txt.format(2.1234))
    # 一些 format 的常用格式

    # f格式化字符串
    name07 = "莫烦Python"
    age07 = 18
    height07 = 1.8
    print(f"我的名字是 {name07} !我 {age07} 岁了，我 {height07} 米高~")
    # 可以在 {} 中进行运算
    print(f"我 {age} 岁了，明年我就{age + 1}岁了~")

    # 支持特殊写法
    score = 2.1234
    print(f"You scored {score:.2%}")
    print(f"You scored {score:.3f}")
    print(f"You scored {12:5d}")


    # 剔除前后空白
    print("  我不想要前后的空白，但是  中间\n的可以有\n  ".strip())
    # 替换文字
    print("帮我替换掉 莫烦".replace("莫烦", "your python"))
    # 文字的大小写处理
    print("How ABOUT lower CaSe?".lower())
    print("And upper CaSe?".upper())
    print("do tiTle For me".title())
    # 拆散你，重组你
    print("你|帮|我|拆分|一下|这句话".split("|"))
    print("|".join(["你", "帮", "我", "重组", "一下", "这句话"]))
    # 街头巷尾遇见你
    print("我在街头看到你".startswith("我在"))
    print("我在街头看到你".startswith("街头"))
    print("我在巷尾看到你".endswith("看到你"))
    print("我在巷尾看到你".endswith("巷尾"))


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('字符串的高级玩法')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
