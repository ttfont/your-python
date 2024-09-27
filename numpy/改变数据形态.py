# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
import numpy as np


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press ⌘F8 to toggle the breakpoint.

    # 改变形态
    # 增加维度
    a = np.array([1, 2, 3, 4, 5, 6])
    a_2d = a[np.newaxis, :]
    print(a, a_2d)
    print(a.shape, a_2d.shape)
    print()
    # 效果相同
    a = np.array([1, 2, 3, 4, 5, 6])
    a_none = a[:, None]
    a_expand = np.expand_dims(a, axis=1)
    print(a_none, a_expand)
    print(a_none.shape, a_expand.shape)
    print()
    # 减少维度
    a_squeeze = np.squeeze(a_expand)
    a_squeeze_axis = a_expand.squeeze(axis=1)
    print(a_squeeze, a_squeeze)
    print(a_squeeze.shape)
    print(a_squeeze_axis.shape)
    print()
    # 改变形态
    a = np.array([1, 2, 3, 4, 5, 6])
    a1 = a.reshape([2, 3])
    a2 = a.reshape([3, 1, 2])
    print("a1 shape:", a1.shape)
    print(a1)
    print("a2 shape:", a2.shape)
    print(a2)
    print()
    # 矩阵转置，np.transpose()
    a = np.array([1, 2, 3, 4, 5, 6]).reshape([2, 3])
    print(a)
    aT1 = a.T
    aT2 = np.transpose(a)

    print(aT1)
    print(aT2)
    print(aT1.shape)
    print(aT2.shape)
    print('合并')
    # 合并
    # 在数据分析统计，机器学习中的数据，都是以二维来存储的。行是数据样本（第一维度），列是特征（第二维度）
    # 将列column合并
    feature_a = np.array([1, 2, 3, 4, 5, 6])
    feature_b = np.array([11, 22, 33, 44, 55, 66])
    c_stack = np.column_stack([feature_a, feature_b])
    print(c_stack)
    # 数据sample和并
    sample_a = np.array([0, 1.1])
    sample_b = np.array([1, 2.2])
    c_stack = np.row_stack([sample_a, sample_b])
    print(c_stack)
    print()
    #  vstack 和 hstack 的时候，先确保维度信息是正确的
    # np.hstack
    feature_a = np.array([1, 2, 3, 4, 5, 6])[:, None]
    feature_b = np.array([11, 22, 33, 44, 55, 66])[:, None]
    c_stack = np.hstack([feature_a, feature_b])
    print(c_stack)
    # np.vstack
    sample_a = np.array([0, 1.1])[None, :]
    print(sample_a.shape)
    sample_b = np.array([1, 2.2])[None, :]
    c_stack = np.vstack([sample_a, sample_b])
    print(c_stack)

    print()
    # np.concatenate() 来处理各种不同情况的合并
    a = np.array([
        [1, 2],
        [3, 4]
    ])
    b = np.array([
        [5, 6],
        [7, 8]
    ])

    print(np.concatenate([a, b], axis=0))
    print(np.concatenate([a, b], axis=1))

    # 拆解
    print('拆解')
    a = np.array(
        [[1, 11, 2, 22],
         [3, 33, 4, 44],
         [5, 55, 6, 66],
         [7, 77, 8, 88]]
    )
    print(np.vsplit(a, indices_or_sections=2))  # 分成两段
    print(np.vsplit(a, indices_or_sections=[2, 3]))  # 分片成 [:2]，[2:3], [3:]
    print()
    # np.vsplit 是拿着刀沿着横向切分，那么 np.hsplit 就是沿纵向切分
    a = np.array(
        [[1, 11, 2, 22],
         [3, 33, 4, 44],
         [5, 55, 6, 66],
         [7, 77, 8, 88]]
    )
    print(np.hsplit(a, indices_or_sections=2))  # 分成两段
    print(np.hsplit(a, indices_or_sections=[2, 3]))  # 分片成 [:2]，[2:3], [3:]
    print()
    # 横切也能纵切的函数 np.split() ，自由分割数组
    a = np.array(
        [[1, 11, 2, 22],
         [3, 33, 4, 44],
         [5, 55, 6, 66],
         [7, 77, 8, 88]]
    )
    print(np.split(a, indices_or_sections=2, axis=0))  # 分成两段
    print(np.split(a, indices_or_sections=[2, 3], axis=1))  # 在第二维度，分片成 [:2]，[2:3]，[3:]


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('改变数据形态')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
