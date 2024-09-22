# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

import threading
import time
from queue import Queue
import copy


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press ⌘F8 to toggle the breakpoint.

    # 添加线程
    # 获取已激活的线程数
    print("已激活的线程数 ", threading.active_count())
    # 查看所有线程信息
    print("所有线程信息 ", threading.enumerate())
    # 查看现在正在运行的线程
    print("现在正在运行的线程 ", threading.current_thread())


def thread_job():
    print(' 1 This is a thread of %s' % threading.current_thread())


def my_thread():
    # target 为目标函数，想要调用的任务方法。name 为当前线程名称。
    thread = threading.Thread(target=thread_job, name='我新建的线程')  # 定义线程
    thread.start()  # 让线程开始工作
    # time.sleep(10)


def thread_job02():
    print(' 2 This is a thread of %s' % threading.current_thread())
    print("thread_job02 T1 start\n")
    for i in range(10):
        time.sleep(0.1)  # 任务间隔0.1s
    print("thread_job02 T1 finish\n")


def job02_thread():
    # join 功能
    # 不加 join 功能
    # 预想的结果
    # T1 start
    # T1 finish
    # all done
    # 实际的结果
    # T1 start
    # all done
    # T1 finish
    added_thread = threading.Thread(target=thread_job02, name='T1')
    added_thread.start()
    # 加 join 功能
    added_thread.join()
    print("job02_thread all done\n")
    # join 控制多个线程的执行顺序


def T1_job():
    print("T1_job T1 start\n")
    for i in range(10):
        time.sleep(0.1)
    print("T1_job T1 finish\n")


def T2_job():
    print("T2_job T2 start\n")
    print("T2_job T2 finish\n")


def T1T2_job_thread():
    thread_1 = threading.Thread(target=T1_job, name='T1')
    thread_2 = threading.Thread(target=T2_job, name='T2')
    thread_1.start()  # 开启T1
    thread_2.start()  # 开启T2
    # 不加 join 打印信息的前后顺序，取决去线程处理数据的速度
    # 在写 join 的时候可以把处理数据量少的写在前面，主要目的是减少主线程或其他依赖线程的等待时间
    thread_2.join()
    thread_1.join()
    print("T1T2_job_thread all done\n")


# 参数 一个列表l和一个队列q
def job(l, q):
    for i in range(len(l)):
        # 给列表元素作平方计算
        l[i] = l[i] ** 2
    q.put(l)  # 多线程调用的函数不能用return返回值


def multithreading():
    q = Queue()  # q中存放返回值，代替return的返回值
    threads = []
    data = [[1, 2, 3], [3, 4, 5], [4, 4, 4], [5, 5, 5]]

    for i in range(4):
        # 定义四个线程, Thread首字母要大写，被调用的job函数没有括号，只是一个索引，参数在后面
        t = threading.Thread(target=job, args=(data[i], q))
        # 开始线程
        t.start()
        # 把每个线程append到线程列表中
        threads.append(t)

    for thread in threads:
        # 阻塞当前线程，主线程暂停执行（或调用 join() 的线程）
        thread.join()
    results = []
    for _ in range(4):
        results.append(q.get())  # q.get()按顺序从q中拿出一个值
    print(results)


def job02(l, q):
    res = sum(l)
    q.put(res)


def multithreading02(l):
    q = Queue()
    threads = []
    for i in range(4):
        t = threading.Thread(target=job02, args=(copy.copy(l), q), name='T%i' % i)
        t.start()
        threads.append(t)
    [t.join() for t in threads]
    total = 0
    for _ in range(4):
        total += q.get()
    print(total)


def normal02(l):
    total = sum(l)
    print(total)


def job1_G():
    global A
    for i in range(10):
        A += 1
        print('job1', A)


def job2_G():
    global A
    for i in range(10):
        A += 10
        print('job2', A)


A = 0
lock = threading.Lock()


def job_1_2_G():
    t1 = threading.Thread(target=job1_G)
    t2 = threading.Thread(target=job2_G)
    t1.start()
    t2.start()
    t1.join()
    t2.join()


def job1_L():
    global A, lock
    lock.acquire()
    try:
        for i in range(10):
            A += 1
            print('job1', A)
    finally:
        lock.release()


def job2_L():
    global A, lock
    # 使用 with 语句可以简化 acquire 和 release 的过程，使代码更简洁清晰。推荐
    with lock:
        for i in range(10):
            A += 10
            print('job2', A)


def job_1_2_L():
    t1 = threading.Thread(target=job1_L)
    t2 = threading.Thread(target=job2_L)
    t1.start()
    t2.start()
    t1.join()
    t2.join()


if __name__ == '__main__':
    print_hi('什么是多线程 Threading')
    my_thread()
    job02_thread()
    T1T2_job_thread()
    multithreading()

    l = list(range(1000000))
    s_t = time.time()
    normal02(l * 4)
    print('normal02: ', time.time() - s_t)
    s_t = time.time()
    multithreading02(l)
    print('multithreading02: ', time.time() - s_t)

    job_1_2_G()
    job_1_2_L()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
