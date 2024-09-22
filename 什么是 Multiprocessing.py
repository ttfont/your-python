# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

import multiprocessing as mp
import threading as td
import time as time


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press ⌘F8 to toggle the breakpoint.

    # 创建进程
    p1 = mp.Process(target=job, args=(1, 2))
    # 启动进程
    p1.start()

    # Shared Value
    value1 = mp.Value('i', 0)
    value2 = mp.Value('d', 3.14)
    # Shared Array，只能是一维数组
    array = mp.Array('i', [1, 2, 3, 4])


def job(a, d):
    print('你好 世界')


# 该函数没有返回值！！！
def job02(q):
    res = 0
    for i in range(1000):
        res += i + i ** 2 + i ** 3
    q.put(res)  #


def my_result_process02():
    q = mp.Queue()
    p1 = mp.Process(target=job02, args=(q,))
    p2 = mp.Process(target=job02, args=(q,))
    p1.start()
    p2.start()
    p1.join()
    p2.join()
    res1 = q.get()
    res2 = q.get()
    print(res1)
    print(res2)
    print(res1 + res2)


def job03(q):
    res = 0
    for i in range(1000000):
        res += i + i ** 2 + i ** 3
    # 结果加 queue
    q.put(res)


# 多核运算多进程
def multicore03():
    q = mp.Queue()
    p1 = mp.Process(target=job03, args=(q,))
    p2 = mp.Process(target=job03, args=(q,))
    p1.start()
    p2.start()
    p1.join()
    p2.join()
    res1 = q.get()
    res2 = q.get()
    print('multicore03:', res1 + res2)


# 单核运算多线程
def multithread03():
    # thread可放入process同样的queue中
    q = mp.Queue()
    t1 = td.Thread(target=job03, args=(q,))
    t2 = td.Thread(target=job03, args=(q,))
    t1.start()
    t2.start()
    t1.join()
    t2.join()
    res1 = q.get()
    res2 = q.get()
    print('multithread03:', res1 + res2)


def normal03():
    res = 0
    for _ in range(2):
        for i in range(1000000):
            res += i + i ** 2 + i ** 3
    print('normal03:', res)


def time_result03():
    st = time.time()
    normal03()
    st1 = time.time()
    print('normal03 time:', st1 - st)
    multithread03()
    st2 = time.time()
    print('multithread03 time:', st2 - st1)
    multicore03()
    print('multicore03 time:', time.time() - st2)


def job04(x):
    # Pool的函数有返回值
    return x * x


def multicore04():
    # Pool的函数有返回值
    pool = mp.Pool()
    # 自分配 CPU 计算
    res = pool.map(job04, range(10))
    print(res)


def multicore05():
    pool = mp.Pool(processes=3)  # 定义CPU核数量为3
    res = pool.map(job04, range(10))
    print(res)


def multicore06():
    pool = mp.Pool()
    # apply_async() 中只能传递一个值，它只会放入一个核进行运算，但是传入值时要注意是可迭代的，
    # 所以在传入值后需要加逗号, 同时需要用get()方法获取返回值
    res = pool.apply_async(job04, (2,))
    # 用get获得结果
    print(res.get())


def multicore07():
    pool = mp.Pool()
    multi_res = [pool.apply_async(job04, (i,)) for i in range(10)]
    # 用get获得结果
    print([res.get() for res in multi_res])


def job08(v, num):
    for _ in range(5):
        time.sleep(0.1)  # 暂停0.1秒，让输出效果更明显
        v.value += num  # v.value获取共享变量值
        print(v.value, end="\n")


def multicore08():
    v = mp.Value('i', 0)  # 定义共享变量
    p1 = mp.Process(target=job08, args=(v, 1))
    p2 = mp.Process(target=job08, args=(v, 3))  # 设定不同的number看如何抢夺内存
    p1.start()
    p2.start()
    p1.join()
    p2.join()


def job09(v, num, l):
    l.acquire()  # 锁住
    for _ in range(5):
        # print(v.value, num)
        time.sleep(0.1)
        v.value = v.value + num  # 获取共享内存
        print(v.value)
    l.release()  # 释放


def multicore09():
    l = mp.Lock()  # 定义一个进程锁
    v = mp.Value('i', 0)  # 定义共享内存

    p1 = mp.Process(target=job09, args=(v, 1, l))  # 需要将lock传入
    p1.start()
    p1.join()

    p2 = mp.Process(target=job09, args=(v, 3, l))
    p2.start()
    p2.join()


def multicore10():
    l = mp.Lock()  # 定义一个进程锁
    v = mp.Value('i', 0)  # 定义共享内存
    p1 = mp.Process(target=job09, args=(v, 1, l))  # 需要将lock传入
    p2 = mp.Process(target=job09, args=(v, 3, l))
    p1.start()
    p2.start()
    p1.join()
    p2.join()


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('什么是 Multiprocessing')
    my_result_process02()
    time_result03()
    multicore04()
    multicore05()
    multicore06()
    multicore07()
    multicore08()
    multicore09()
    # multicore10()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
