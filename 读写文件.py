# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press ⌘F8 to toggle the breakpoint.
    # 创建文件，创建的文件会在当前目录中
    f = open("new_file.txt", "w")  # 创建并打开
    f.write("some text...")  # 在文件里写东西
    f.close()

    # 如果怕自己忘记 close() ，可以用 with 的模式，with 架构把打开和关闭嵌入到了其中
    with open("new_file2.txt", "w") as f:
        f.writelines(["some text for file2...\n", "2nd line\n"])

    # 读文件
    f = open("new_file2.txt", "r")
    print(f.read())
    f.close()

    with open("new_file2.txt", "r") as f:
        print(f.readlines())
        # list01 = f.readlines()
        # print(list01)
        print()
    with open("new_file3.txt", "r") as f:
        while True:
            line = f.readline()
            print(line)
            print(not line)
            if not line:
                break

    # 文件编码，中文乱码
    print()
    with open("chinese.txt", "wb") as f:
        f.write("这是中文的，this is Chinese".encode("gbk"))

    with open("chinese.txt", "rb", ) as f:
        # print(f.read()) 不指定编码时为乱码
        print(f.read().decode('gbk'))  # windows在本机尝试，可以试试这个

    # 下面的代码会报错，如果直接用原始的 r 来读文本
    # UnicodeDecodeError: 'utf-8' codec can't decode byte 0xd5 in position 0: invalid continuation byte
    # with open("chinese.txt", "r") as f:
    #     print(f.read())
    # 传入正确的文件编码
    with open("chinese.txt", "r", encoding="gbk") as f:
        print(f.read())

    # 更多读写模式
    # mode	意思
    # w	（创建）写文本
    # r	读文本，文件不存在会报错
    # a	在文本最后添加
    # wb	写二进制 binary
    # rb	读二进制 binary
    # ab	添加二进制
    # w+	又可以读又可以（创建）写
    # r+	又可以读又可以写, 文件不存在会报错
    # a+	可读写，在文本最后添加
    # x	创建

    with open("new_file3.txt", "r") as f:
        print(f.read())
    with open("new_file4.txt", "r+") as f:
        f.write("text has been replaced")
        f.seek(0)       # 将开始读的位置从写入的最后位置调到开头
        print(f.read())
    with open("new_file5.txt", "a+") as f:
        print(f.read())
        f.write("\nadd new line")
        f.seek(0)       # 将开始读的位置从写入的最后位置调到开头
        print(f.read())


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('读写文件')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
