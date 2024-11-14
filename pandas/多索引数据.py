# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
import pandas as pd


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press ⌘F8 to toggle the breakpoint.
    # 构建Row多索引
    s = pd.Series(
        ["小米", "小明",  # 一年一班
         "小命", "小勉",  # 一年二班
         "小牛", "小鸟",  # 二年一班
         "小南", "小妮"  # 二年二班
         ], name="name")
    print(s)
    tuples = [
        # 年级，班级
        ("one", "1"),
        ("one", "1"),
        ("one", "2"),
        ("one", "2"),
        ("two", "1"),
        ("two", "1"),
        ("two", "2"),
        ("two", "2"),
    ]
    index = pd.MultiIndex.from_tuples(
        tuples, names=["grade", "class"])
    print(index)
    s = pd.Series(
        ["小米", "小明",  # 一年一班
         "小命", "小勉",  # 一年二班
         "小牛", "小鸟",  # 二年一班
         "小南", "小妮"  # 二年二班
         ], name="name", index=index)
    print(s)
    print()
    print(s.index)
    iterables = [
        ["one", "two"],  # 年级
        ["1", "1", "2", "2"]  # 每个学生所在班级
    ]

    index2 = pd.MultiIndex.from_product(
        iterables, names=["grade", "class"])
    print(index2)
    s2 = pd.Series(
        ["小米", "小明",  # 一年一班
         "小命", "小勉",  # 一年二班
         "小牛", "小鸟",  # 二年一班
         "小南", "小妮"  # 二年二班
         ],
        name="name",
        index=index2)
    print(s2)
    df = pd.DataFrame(
        [
            # 年级，班级
            ("one", "1"),
            ("one", "1"),
            ("one", "2"),
            ("one", "2"),
            ("two", "1"),
            ("two", "1"),
            ("two", "2"),
            ("two", "2"),
        ],
        columns=["grade", "class"]
    )

    index3 = pd.MultiIndex.from_frame(df)
    print(index3)
    s3 = pd.Series(
        ["小米", "小明",  # 一年一班
         "小命", "小勉",  # 一年二班
         "小牛", "小鸟",  # 二年一班
         "小南", "小妮"  # 二年二班
         ],
        name="name",
        index=index3)
    print(s3)

    # 构建DataFrame多索引
    df1 = pd.DataFrame(
        {"id": [11, 12, 13, 14, 15, 16, 17, 18],
         "name":
             ["小米", "小明",  # 一年一班
              "小命", "小勉",  # 一年二班
              "小牛", "小鸟",  # 二年一班
              "小南", "小妮"  # 二年二班
              ]},
        index=index)
    print(df1)

    # 构建Column多索引
    df2 = pd.DataFrame(
        [[11, 12, 13, 14, 15, 16, 17, 18],
         ["小米", "小明",  # 一年一班
          "小命", "小勉",  # 一年二班
          "小牛", "小鸟",  # 二年一班
          "小南", "小妮"  # 二年二班
          ]],
        index=["id", "name"])
    print(df2)
    df2 = pd.DataFrame(
        [[11, 12, 13, 14, 15, 16, 17, 18],
         ["小米", "小明",  # 一年一班
          "小命", "小勉",  # 一年二班
          "小牛", "小鸟",  # 二年一班
          "小南", "小妮"  # 二年二班
          ]],
        index=["id", "name"],
        columns=index,  # 多索引加这
    )
    print(df2)
    print()
    # 选择数据
    df3 = pd.DataFrame(
        [[11, 12, 13, 14, 15, 16, 17, 18],
         ["小米", "小明",  # 一年一班
          "小命", "小勉",  # 一年二班
          "小牛", "小鸟",  # 二年一班
          "小南", "小妮"  # 二年二班
          ]],
        index=["id", "name"],
        columns=index,  # 多索引加这
    )
    print(df3)
    # 获取一年级数据
    print(df3["one"])
    # 获取一年级 1 班数据
    print(df3["one"]["1"])

    df4 = pd.DataFrame(
        {"id": [11, 12, 13, 14, 15, 16, 17, 18],
         "name":
             ["小米", "小明",  # 一年一班
              "小命", "小勉",  # 一年二班
              "小牛", "小鸟",  # 二年一班
              "小南", "小妮"  # 二年二班
              ]},
        index=index)
    print(df4)
    print(df4.loc["one"].loc["2"])


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('多索引数据')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
