# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

import numpy as np
import matplotlib.pyplot as plt

def relu(x):
    return np.maximum(0, x)

def tanh(x):
    return np.tanh(x)

# 定义一个函数来创建神经网络层
def layer(in_dim, out_dim):
    # 生成权重数组，权重初始值来自均值为0，标准差为0.1的正态分布
    weights = np.random.normal(loc=0, scale=0.1, size=[in_dim, out_dim])
    # 生成偏置数组，每个偏置的初始值为0.1
    bias = np.full([1, out_dim], 0.1)
    # 返回包含权重和偏置的字典
    return {"w": weights, "b": bias}


def draw_scatter(x, y):
    # 使用 matplotlib 的 scatter 方法来绘制散点图
    # x.ravel() 和 y.ravel() 将 x 和 y 的二维数组转换为一维数组，适合作为散点图的输入
    plt.scatter(x.ravel(), y.ravel())
    # 显示图表
    plt.show()


def sigmoid(x):
    return 1 / (1 + np.exp(-x))


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press ⌘F8 to toggle the breakpoint.
    # 回顾矩阵运算
    # 矩阵的点乘

    data = np.random.rand(4, 3)
    weights = np.random.rand(3, 2)
    output = np.dot(data, weights)

    print("data shape:", data.shape)
    print("weights shape:", weights.shape)
    print("output shape:", output.shape)
    # 4 * 3 的矩阵点乘一个 3 * 2 的矩阵，结果会是 4 * 2 的矩阵。

    # 神经网络的分类与回归
    # 分类
    student = np.array([[1, 2, 3]])
    model = np.random.rand(3, 1)
    score = np.dot(student, model)
    print(score)
    # 回归
    student = np.array([[0.1, 0.2, -0.3]])
    model = np.random.rand(3, 1)
    output = np.dot(student, model)

    # 用 level 表示是否及格
    result = sigmoid(output)
    print(result)
    if result < 0.5:
        level = "不及格"
    else:
        level = "及格"
    print(level)
    # 多层神经网络前向
    # 数据生成部分
    # x 是从 -1 到 1 之间均匀分布的 10 个点，[:, None] 将一维数组转换为二维数组，形状为 [10, 1]
    x = np.linspace(-1, 1, 10)[:, None]
    # y 是生成的噪声数据，基于 x 的值并添加以 0 为均值，0.2 为标准差的正态分布噪声
    y = np.random.normal(loc=0, scale=0.2, size=[10, 1]) + x

    # 调用函数 draw_scatter 来绘制 x 和 y 的散点图
    # draw_scatter(x, y)

    # 创建第一层网络，输入维度为1，输出维度为3
    l1 = layer(1, 3)
    # 创建第二层网络，输入维度为3，输出维度为1
    l2 = layer(3, 1)

    # 使用输入数据x进行第一层的前向传播计算
    o = x.dot(l1["w"]) + l1["b"]  # 矩阵乘法和偏置相加
    print("第一层出来后的 shape:", o.shape)  # 打印第一层输出的数据形状

    # 使用第一层的输出作为第二层的输入，进行第二层的前向传播计算
    o = o.dot(l2["w"]) + l2["b"]  # 矩阵乘法和偏置相加
    print("第二层出来后的 shape:", o.shape)  # 打印第二层输出的数据形状

    print("output:", o)  # 打印最终输出结果

    # 使用自定义的draw_scatter函数，以x为横坐标，最终输出o为纵坐标绘制散点图
    # draw_scatter(x, o)

    # 第一层
    o = x.dot(l1["w"]) + l1["b"]

    # 可以在这里添加激活函数，增强非线性拟合能力
    o = relu(o)

    # 第二层
    o = o.dot(l2["w"]) + l2["b"]

    print(o.shape)
    draw_scatter(x, o)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('神经网络-矩阵运算')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
