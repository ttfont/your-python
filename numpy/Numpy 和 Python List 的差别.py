# This is a sample Python script.
import numpy as np
import time


# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press ⌘F8 to toggle the breakpoint.
    # 主要涉及内容
    # Numpy Array
    # np.array()
    print(np.array([1, 2, 3]))

    # List 和 Numpy array 共同点，
    # List 存取数据
    my_list = [1, 2, 3]
    print(my_list[0])
    # numpy 存取数据
    my_array = np.array([1, 2, 3])
    print(my_array[0])
    # 对值进行修改
    my_list[0] = -1
    my_array[0] = -1
    print(my_list)
    print(my_array)

    # Numpy 的优势
    # Numpy 在内存中连续的一块物理地址存储数据。
    # Python 的 List 并不是连续存储的，
    # NumPy 数组的确主要是用于存储同种数据类型的元素，这种设计使得它在进行批量计算时比 Python 的原生列表要高效得多。
    # 对比运行时间
    list_and_numpy()
    # map 来代替 Python 的原生循环
    map_and_numpy()


def list_and_numpy():
    t0 = time.time()
    # python list
    l = list(range(100))
    for _ in range(10000):
        for i in range(len(l)):
            l[i] += 1

    t1 = time.time()
    # numpy array
    a = np.array(l)
    for _ in range(10000):
        a += 1

    print("Python list spend {:.3f}s".format(t1 - t0))
    print("Numpy array spend {:.3f}s".format(time.time() - t1))


def map_and_numpy():
    t0 = time.time()
    # python list
    l = list(range(100))
    for _ in range(10000):
        l = list(map(lambda i: i + 1, l))

    t1 = time.time()
    # numpy array
    a = np.array(l)
    for _ in range(10000):
        a += 1

    print("Python list with map spend {:.3f}s".format(t1 - t0))
    print("Numpy array spend {:.3f}s".format(time.time() - t1))


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('numpy')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
