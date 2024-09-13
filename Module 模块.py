# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press ⌘F8 to toggle the breakpoint.

# 文件中的代码 module 中的 file.py

# 引用 module, 可以表述为 引用库，引用包，引用代码
# me.py

# 引用 module 这里时 me.py 中的内容 start
# 第一种
import file

print("1", file.create_name())

# 第二种更偷懒
from file import *

print("2", create_name())
print("2", create_time())

# 给模块重命名
import file as f1

print("f1:", f1.create_name())

# 从模块中引用函数
from file import create_name

print(create_name())

# 从模块中引用多个函数
from file import create_name, create_time

print(create_name(), create_time())


class File02:
    def create_name(self):
        return "new_file02.txt"


f2 = File02()
print("f2:", f2.create_name())

from module.files import get_video_size

print(f"get_video_size = ", get_video_size())


# from files import create_name    # 这里会报错
# 获取到 text.py 的功能
import module.files.text

print(module.files.text.create_name())

# 或者这样：
from module.files import text

print(text.create_name())

# 引用 module 这里时 me.py 中的内容 end


# 大项目的模块管理
# 见 module 中的 files

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('Module 模块')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
