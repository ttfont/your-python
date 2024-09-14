# This is a sample Python script.
import os
import shutil


# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
def copy(path):
    filename = os.path.basename(path)  # 文件名
    dir_name = os.path.dirname(path)  # 文件夹名
    new_filename = "new_" + filename  # 新文件名
    new_path = os.path.join(dir_name, new_filename)  # 目录重组
    shutil.copy2(path, new_path)  # 复制文件
    return os.path.isfile(new_path), new_path


def copyBySplit(path):
    dir_name, filename = os.path.split(path)
    new_filename = "new2_" + filename    # 新文件名
    new_path = os.path.join(dir_name, new_filename) # 目录重组
    shutil.copy2(path, new_path)   # 复制文件
    return os.path.isfile(new_path), new_path



def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press ⌘F8 to toggle the breakpoint.
    # 主要涉及到的功能：

    # 文件目录操作
    # os.getcwd()
    # os.listdir()
    # os.makedirs()
    # os.path.exists()

    # 文件管理系统
    # os.removedirs()
    # shutil.rmtree()
    # os.rename()

    # 文件目录多种检验
    # os.path.isfile()
    # os.path.exists()
    # os.path.isdir()
    # os.path.basename()
    # os.path.dirname()
    # os.path.split()

    # os库
    # 文件目录操作
    print("当前目录：", os.getcwd())
    print("当前目录里有什么：", os.listdir())
    # 在当前目录新建 project 目录
    os.makedirs("project", exist_ok=True)
    print(os.path.exists("project"))

    # 文件管理系统
    # 创建文件夹
    if os.path.exists("user/mofan"):
        print("user exist")
    else:
        os.makedirs("user/mofan")
        print("user created")
    # user 目录下有什么
    print(os.listdir("user"))

    # 删除文件夹，user会一并删除
    if os.path.exists("user/mofan"):
        # os.removedirs("user/mofan")
        print("user removed")
    else:
        print("user not exist")

    # 文件夹里有文件删除时会报错
    os.makedirs("user/mofan01", exist_ok=True)
    with open("user/mofan01/a.txt", "w") as f:
        f.write("nothing")
    # os.removedirs("user/mofan01")  # 这里会报错

    # 清空整个目录，user 的子目录会被清空，无论存不存文件，慎用
    shutil.rmtree("user/mofan01")
    print(os.listdir("user"))

    # 修改文件夹名字
    os.makedirs("user/mofan", exist_ok=True)
    # os.rename("user/mofan", "user/mofanpy")
    print(os.listdir("user"))

    # 文件目录多种检验，判断是否时文件或者目录
    os.makedirs("user/mofan", exist_ok=True)
    with open("user/mofan/a.txt", "w") as f:
        f.write("nothing")
    print(os.path.isfile("user/mofan/a.txt"))  # True
    print(os.path.exists("user/mofan/a.txt"))  # True
    print(os.path.isdir("user/mofan/a.txt"))  # False
    print(os.path.isdir("user/mofan"))  # True
    # 创建一个文件副本
    copied, new_path = copy("user/mofanpy01/a.txt")
    if copied:
        print("copied to:", new_path)
    else:
        print("copy failed")
    # 使用 os.path.split(path) 创建文件副本
    copied, new_path = copyBySplit("user/mofanpy02/a.txt")
    if copied:
        print("copied to:", new_path)
    else:
        print("copy failed")


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('文件目录管理')

    # See PyCharm help at https://www.jetbrains.com/help/pycharm/

