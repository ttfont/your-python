# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
import re
import time


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press ⌘F8 to toggle the breakpoint.
    # 正则表达式 在各大开发语言中都是通用的，一式在手天下我有
    # 这一节主要涉及到的功能：
    # 不用正则的判断
    # re.compile()
    # ptn.search()
    # 正则给额外信息
    # re.search()
    # 中文
    # string.encode()
    # 查找替换等更多功能
    # re.search()
    # re.match()
    # re.findall()
    # re.finditer()
    # re.split()
    # re.sub()
    # re.subn()

    # 不用正则的判断
    pattern1 = "file"
    pattern2 = "files"
    string = "the file is in the folder"
    print("file in string", pattern1 in string)
    print("files in string", pattern2 in string)
    print()
    # 验证用户输入的信息是否是邮箱
    ptn = re.compile(r"\w+?@\w+?\.com")

    matched = ptn.search("mofan@mofanpy.com")
    print("mofan@mofanpy.com is a valid email:", matched)
    matched = ptn.search("mofan@mofanpy+com")
    print("mofan@mofanpy+com is a valid email:", matched)
    print()
    # 正则给额外信息
    matched = re.search(r"\w+?@\w+?\.com", "mofan@mofanpy.com")
    print("mofan@mofanpy.com:", matched)
    # mofan@mofanpy.com: <re.Match object; span=(0, 17), match='mofan@mofanpy.com'>
    # 打印的参数中 span 是从哪一位到哪一位(0, 17)，match表示找到的具体字符串又是什么。
    matched = re.search(r"\w+?@\w+?\.com", "the email is mofan@mofanpy.com.")
    print("the email is mofan@mofanpy.com:", matched)
    # 一个简单的例子，r"xxx" 为固定写法
    match = re.search(r"run", "I run to you")
    print(match)
    print(match.span())
    print(match.group())

    # 同时满足多种条件，多次匹配
    print(re.search(r"ran", "I run to you"))
    print(re.search(r"run", "I run to you"))
    # 同时满足多种条件，一次匹配, | 就代表或者; [au] 中间字母是 a 或者 u
    print(re.search(r"ran|run", "I run to you"))
    print(re.search(r"r[au]n", "I run to you"))
    # 同时满足多种条件，前后都是固定的,同时满足多个字符的不同匹配,比如找到 find 和 found
    print(re.search(r"f(ou|i)nd", "I find you"))
    print(re.search(r"f(ou|i)nd", "I found you"))
    print()
    # 按类型匹配，通用匹配方式
    # 特定标识	含义	范围
    # \d	任何数字	[0-9]
    # \D	不是数字的
    # \s	任何空白字符	[ \t\n\r\f\v]
    # \S	空白字符以外的
    # \w	任何大小写字母,数字和 _	[a-zA-Z0-9_]
    # \W	\w 以外的
    # \b	匹配一个单词边界	比如 er\b 可以匹配 never 中的 er，但不能匹配 verb 中的 er
    # \B	匹配非单词边界	比如 er\B 能匹配 verb 中的 er，但不能匹配 never 中的 er
    # \\	强制匹配 \
    # .	匹配任何字符 (除了 \n)
    # ?	前面的模式可有可无
    # *	重复零次或多次
    # +	重复一次或多次
    # {n,m}	重复 n 至 m 次
    # {n}	重复 n 次
    # +?	非贪婪（匹配尽可能少的字符），最小方式匹配 +
    # *?	非贪婪（匹配尽可能少的字符），最小方式匹配 *
    # ??	非贪婪（匹配尽可能少的字符），最小方式匹配 ?
    # ^	匹配一行开头，在 re.M 下，每行开头都匹配
    # $	匹配一行结尾，在 re.M 下，每行结尾都匹配
    # \A	匹配最开始，在 re.M 下，也从文本最开始
    # \B	匹配最结尾，在 re.M 下，也从文本最结尾

    # 匹配邮箱 ，\w 表示任意的字母和数字下划线。 +? 表示让 \w 至少匹配 1 次
    re.search(r"\w+?@\w+?\.com", "mofan@mofanpy.com")
    # 匹配手机号
    # \d{8} 表示任意的数字，重复8遍。
    print(re.search(r"138\d{8}", "13812345678"))
    print(re.search(r"138\d{8}", "138123456780000"))
    print()
    # 匹配中文 ?爱 表示爱前面的字符可有可无
    print(re.search(r"不?爱", "我爱你"))
    # 匹配中文 不?爱 表示爱前面的字符可有可无，有不就匹配
    print(re.search(r"不?爱", "我不爱你"))
    # 匹配中文 不.*?爱 表示 不 必须匹配, .* 匹配任何字符 (除了 \n)重复零次或多次, 爱前面的字符可有可无
    print(re.search(r"不.*?爱", "我不是很爱你"))
    print()
    # 匹配全部汉字，汉字是用 Unicode 来表示的，把汉字变成 Unicode
    print("中".encode("unicode-escape"))
    print(re.search(r"[\u4e00-\u9fa5]+", "我爱编码，Python。"))
    # 匹配全部汉字，识别中文标点，比如 [！？。，￥【】「」]
    print(re.search(r"[\u4e00-\u9fa5！？。，￥【】「」]+", "我爱编码。编码让人「神清气爽」！haha"))
    print()

    # 查找替换等更多功能
    # 扫描查找整个字符串，找到第一个模式匹配的
    print("search:", re.search(r"run", "I run to you"))
    # 从字符的最开头匹配，找到第一个模式匹配的即使用 re.M 多行匹配，也是从最最开头开始匹配
    print("match:", re.match(r"run", "I run to you"))
    # 返回一个不重复的 pattern 的匹配列表
    print("findall:", re.findall(r"r[ua]n", "I run to you. you ran to him"))
    # 和 findall 一样，只是用迭代器的方式使用
    for i in re.finditer(r"r[ua]n", "I run to you. you ran to him"):
        print("finditer:", i)
    # 用正则分开字符串
    print("split:", re.split(r"r[ua]n", "I run to you. you ran to him"))
    # 用正则替换字符
    print("sub:", re.sub(r"r[ua]n", "jump", "I run to you. you ran to him"))
    # 和 sub 一样，额外返回一个替代次数
    print("subn:", re.subn(r"r[ua]n", "jump", "I run to you. you ran to him"))
    print()

    # 在模式中获取特定信息， 找到 *.jpg 图片文件，而且只返回去掉 .jpg 之后的纯文件名
    found = []
    for i in re.finditer(r"[\w-]+?\.jpg", "I have 2021-02-01.jpg, 2021-02-02.jpg, 2021-02-03.jpg"):
        found.append(re.sub(r".jpg", "", i.group()))
    print(found)
    print()
    # () 提取匹配的字符串：要截取返回的位置，直接返回括号里的内容。
    string = "I have 2021-02-01.jpg, 2021-02-02.jpg, 2021-02-03.jpg"
    print("without ():", re.findall(r"[\w-]+?\.jpg", string))
    print("with ():", re.findall(r"([\w-]+?)\.jpg", string))
    print()
    string = "I have 2021-02-01.jpg, 2021-02-02.jpg, 2021-02-03.jpg"
    match = re.finditer(r"(\d+?)-(\d+?)-(\d+?)\.jpg", string)
    for file in match:
        print("matched string:", file.group(0), ",year:", file.group(1), ", month:", file.group(2), ", day:",
              file.group(3))
    print()
    string = "I have 2021-02-01.jpg, 2021-02-02.jpg, 2021-02-03.jpg"
    match = re.findall(r"(\d+?)-(\d+?)-(\d+?)\.jpg", string)
    for file in match:
        print("year:", file[0], ", month:", file[1], ", day:", file[2])
    print()
    # 索引名字
    string = "I have 2021-02-01.jpg, 2021-02-02.jpg, 2021-02-03.jpg"
    match = re.finditer(r"(?P<y>\d+?)-(?P<m>\d+?)-(?P<d>\d+?)\.jpg", string)
    for file in match:
        print("matched string:", file.group(0),
              ", year:", file.group("y"),
              ", month:", file.group("m"),
              ", day:", file.group("d"))
    print()
    # 多模式匹配
    # re.I 忽略大小写
    # re.M 多行模式，改变'^'和'$'的行为，标志意味着 ^ 和 $ 分别匹配输入字符串的开始处和结束处，以及每一行的开始和结束处。
    # re.S 点任意匹配模式，改变'.'的行为, 使".“可以匹配任意字符
    # re.L 使预定字符类 \w \W \b \B \s \S 取决于当前区域设定
    # re.U 使预定字符类 \w \W \b \B \s \S \d \D 取决于unicode定义的字符属性
    # re.X 详细模式。这个模式下正则表达式可以是多行，忽略空白字符，并可以加入注释。以下两个正则表达式是等价的
    ptn, string = r"r[ua]n", "I Ran to you"
    print("without re.I:", re.search(ptn, string))
    print("with re.I:", re.search(ptn, string, flags=re.I))
    print()

    ptn02 = r"^ran"
    # 多行字符串匹配得顶格写，否则前面有空格或缩进，无法匹配， ^ 要求 "ran" 必须在新行的最开始处。
    string02 = """I
ran to you"""
    print("without re.M:", re.search(ptn02, string02))
    print("with re.M:", re.search(ptn02, string02, flags=re.M))
    print("with re.M and match:", re.match(ptn02, string02, flags=re.M))

    print()
    ptn03 = r"^ran"
    string03 = """I
Ran to you"""
    print("with re.M and re.I:", re.search(ptn03, string03, flags=re.M | re.I))

    print()
    string04 = """I
Ran to you"""
    print(re.search(r"(?im)^ran", string04))
    print()

    # 更快地执行,先 compile 正则

    n = 1000000
    # 不提前 compile
    t0 = time.time()
    for _ in range(n):
        re.search(r"ran", "I ran to you")
    t1 = time.time()
    print("不提前 compile 运行时间：", t1 - t0)

    # 先做 compile
    ptn = re.compile(r"ran")
    for _ in range(n):
        ptn.search("I ran to you")
    print("提前 compile 运行时间：", time.time() - t1)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('正则表达式')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
