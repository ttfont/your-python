# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
import pandas as pd
import matplotlib.pyplot as plt


def get_xy(df):
    return df[["sepal length", "sepal width", "petal length", "petal width"]], df[["class"]]


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press ⌘F8 to toggle the breakpoint.
    # 加载数据
    columns = ["sepal length", "sepal width", "petal length", "petal width", "class"]
    df = pd.read_csv("data/iris.csv", names=columns)
    print(df)
    # NaN数据处理
    print(df.isna())
    print(df.isna().any())
    print(df.loc[pd.isna(df["petal width"])])
    df1 = df.dropna(axis=0, how="any")
    print(df1)
    print(df1.isna().any())
    # 异常值处理
    df1.plot()
    plt.show()
    df1["sepal length"].plot()
    plt.show()
    index = df1[df1["sepal length"] < 0].index
    df2 = df1.drop(index)
    df2["sepal length"].plot()
    plt.show()
    df2["sepal length"].hist(bins=20)
    plt.show()
    # 切分训练和测试数据
    total_data = len(df2)
    n_train = int(total_data * 0.8)

    train_data = df2.iloc[:n_train]
    print(train_data)
    test_data = df2.iloc[n_train:]
    print(test_data)
    df3 = df2.sample(frac=1)
    print(df3)
    train_data = df3.iloc[:n_train]
    print(train_data)
    test_data = df3.iloc[n_train:]
    print(test_data)

    # 切分标签数据
    print(train_data.loc[:, "class"])

    train_x, train_y = get_xy(train_data)
    print(train_x.head())
    print(train_y.head())

    test_x, test_y = get_xy(test_data)
    print(test_x.head())
    print(test_y.head())

    train_x_array, train_y_array = train_x.values, train_y.values
    print(train_x_array[:3])


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('机器学习数据预处理')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
