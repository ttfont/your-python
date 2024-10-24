# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
import pandas as pd
import numpy as np


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press ⌘F8 to toggle the breakpoint.
    # python、numpy 和 pandas 对比
    # List 和 Dictionary
    a_list = [1, 2, 3]
    a_dict = {"a": 1, "b": 2, "c": 3}
    print("list:", a_list)
    print("dict:", a_dict)
    # numpy array
    a_array = np.array([
        [1, 2],
        [3, 4]
    ])
    # pandas DataFrame
    a_df = pd.DataFrame(
        {"a": [1, 3],
         "b": [2, 4]}
    )

    print("numpy array:\n", a_array)
    print("\npandas df:\n", a_df)
    # Pandas 是 Numpy 的封装库，继承了 Numpy 的很多优良传统，也具备丰富的功能组件.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('Pandas 和 Numpy 的差别')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
