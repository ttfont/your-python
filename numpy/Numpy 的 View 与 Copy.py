# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
import numpy as np
import timeit
from functools import partial


def get_run_time(func, *args):
    repeat = 3
    number = 200
    return min(timeit.Timer(partial(func, *args)).repeat(repeat=repeat, number=number)) / number


a = np.random.rand(1000, 1000)
b = np.random.rand(1000, 1000)


def f1():
    global b
    # 这会产生新的 b
    b = 2 * b


def f2():
    global a
    # 这不会产生新的 a
    a *= 2  # 和 a[:] *= 2 一样


def f11():
    a.flatten()


def f22():
    b.ravel()


a000 = np.random.rand(1000000, 10)
indices = np.random.randint(0, len(a000), size=10000)


def f111():
    # fancy indexing
    _ = a000[indices]
    # print("a000[indices] = ", _)


def f222():
    # take
    _ = np.take(a000, indices, axis=0)
    # print("np.take(a000, indices, axis=0) = ", _)


a111 = np.random.rand(10000, 10)
mask = a111[:, 0] < 0.5


def f1111():
    _ = a111[mask]


def f2222():
    _ = np.compress(mask, a111, axis=0)


a222 = np.zeros([10000, 10])


def f11111(a222):
    a222 = a222 + 1


def f22222(a222):
    a222 = np.add(a222, 1)


aa = np.zeros([1000, 1000])
bb = np.zeros_like(aa)
cc = np.zeros_like(aa)


def f1a():
    aa[:] = np.add(aa, 1)  # 把计算结果赋值回原数据


def f2b():
    np.add(bb, 1, out=bb)  # 把计算结果赋值回原数据


def f3c():
    _cc = np.add(cc, 1)  # 把计算结果赋值到新数据


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press ⌘F8 to toggle the breakpoint.

    a = np.arange(1, 7).reshape((3, 2))
    a_view = a[:2]
    a_copy = a[:2].copy()
    print(a_view, a_copy)
    a_copy[1, 1] = 0
    print("在 copy 上修改数据，不会影响源数据：\n", a)

    a_view[1, 1] = 0
    print("在 view 上修改数据，会影响'窗里'的源数据：\n", a)

    print('%.6f - b = 2*b' % get_run_time(f1))
    print('%.6f - a *= 2' % get_run_time(f2))
    print()
    # 总是 Copy
    print('%.6f - flatten' % get_run_time(f11))
    # 用 ravel(), 需要 copy 的时候才会被 copy
    print('%.6f - ravel' % get_run_time(f22))

    # 在选择数据上加速
    a = np.zeros([100, 100])
    # a = np.random.rand(10, 6)
    print(a)

    # 切片的操作是  view
    a_view1 = a[1:2, 3:6]  # 切片 slice
    a_view2 = a[:10]  # 同上
    a_view3 = a[::2]  # 跳行
    a_view4 = a.ravel()  # 上面提到了
    print("a_view1 = ", a_view1)
    print("a_view2 = ", a_view2)
    print("a_view3 = ", a_view3)
    print("a_view4 = ", a_view4)
    print()
    # 花式索引访问的方式是 copy
    # a = np.zeros([2, 2])
    a = np.random.rand(2, 2)
    print("a = ", a)
    a_copy2 = a[[True, True], [False, True]]  # 用 mask
    print("a_copy2 = ", a_copy2)
    a = np.zeros([100, 100])
    a_copy1 = a[[1, 4, 6], [2, 4, 6]]  # 用 index 选
    a_copy3 = a[[1, 2], :]  # 虽然 1,2 的确连在一起了, 但是他们确实是 copy
    a_copy4 = a[a[1, :] != 0, :]  # fancy indexing
    a_copy5 = a[np.isnan(a[:, 0]), :]  # fancy indexing
    print("a_copy1 = ", a_copy1)
    print("a_copy3 = ", a_copy3)
    print("a_copy4 = ", a_copy4)
    print("a_copy5 = ", a_copy5)
    print()
    # 优化copy的方法
    # 1. 使用 np.take(), 替代用 index 选数据的方法。
    print("len(a000) = ", len(a000))
    print("indices = ", indices)
    print('%.6f - [indices]' % get_run_time(f111))
    print('%.6f - take' % get_run_time(f222))
    print()
    # 2. 使用 np.compress(), 替代用 mask 选数据的方法。
    print('%.6f - [mask]' % get_run_time(f1111))
    print('%.6f - compress' % get_run_time(f2222))
    print()
    # 非常有用的 out 参数
    print('%.6f - a + 1' % get_run_time(f11111, a222))
    print('%.6f - np.add(a, 1)' % get_run_time(f22222, a222))

    a = np.zeros([2, ])
    a_copy = np.add(a, 1)  # copy 发生在这里
    print(a, a_copy)

    b = np.zeros([2, ])
    c = np.zeros_like(b)  # copy 发生在这里
    np.add(b, 1, out=c)
    print(b, c)

    print()
    print('%.6f - without out' % get_run_time(f1a))
    print('%.6f - out' % get_run_time(f2b))
    print('%.6f - new data' % get_run_time(f3c))


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('Numpy 的 View 与 Copy')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
