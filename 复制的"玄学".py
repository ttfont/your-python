# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press ⌘F8 to toggle the breakpoint.
    # 我的确复制了呀, 复制数值
    # 复制本质是复制地址和复制值
    l = [1, 2, 3]
    _l = l.copy()
    _l[0] = -1
    print(_l)
    print(l)
    # 看看这个示例
    l = [[1], [2], 3]
    _l = l.copy()
    _l[0][0] = -1
    print(_l)
    print(l)
    # 运行后，发现，源列表居然变了，再来看一个实例
    audio = File("mp3")
    file = File("txt")
    l = [audio, file]
    _l = l.copy()
    _l[0].name = "mp4"
    print(audio.name)  # "mp4"
    # 源列表是 mp3 的，怎么被复制后的列表改变成了 mp4
    # Python 中复制，有两种方式，一种是深拷贝，一种是浅拷贝。
    # 深拷贝与浅拷贝
    # 深拷贝是 Deep Copy，浅拷贝是 Shallow Copy
    # Deep copy 就是我们通常意义上的复制，把东西全部再造了一遍，彻底成为了两个独立的个体。 而
    # Shallow Copy, 其实也有一点影子拷贝的意思，我复制出来的是你的一个影子，一个投影成像。 所以真实的实体是没有被复制的，我只复制了这个实体的一个投影而已。
    # Python 对数值字符的复制，直接是复制的值
    # 对存放实例的列表做 Deep Copy 深拷贝
    from copy import deepcopy
    l = [[1], [2], 3]
    _l = deepcopy(l)
    _l[0][0] = -1
    print(_l)
    print(l)


class File:
    def __init__(self, name):
        self.name = name


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('复制的"玄学"')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
