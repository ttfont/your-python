# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
import pandas as pd


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press ⌘F8 to toggle the breakpoint.
    # Excel文件
    # pd.read_excel()
    # df.to_excel()
    # csv或txt等纯文本文件
    # pd.read_csv()
    # df.to_csv()
    # 其他有趣的
    # pd.read_clipboard()
    # pd.read_html()

    df = pd.read_excel("./data/体检数据.xlsx", index_col=0)
    print(df)
    df.loc[2, "体重"] = 1
    print(df)
    df.to_excel("data/体检数据_修改.xlsx")
    print(pd.read_excel("data/体检数据_修改.xlsx", index_col=0))
    # csv或txt等纯文本文件
    # Python 打开文件
    with open("data/体检数据.csv", "r", encoding="utf-8") as f:
        print(f.read())
    # Pandas 打开csv
    df_csv = pd.read_csv("data/体检数据.csv", index_col=0)
    print(df_csv)
    # Pandas 打开特殊字符分隔的文件
    with open("data/体检数据_sep.csv", "r", encoding="utf-8") as f:
        print(f.read())
    df_csv = pd.read_csv("data/体检数据_sep.csv", index_col=0, sep="=")
    print(df_csv)
    # 打开 txt 文件
    with open("data/体检数据_sep.txt", "r", encoding="utf-8") as f:
        print(f.read())
    df_txt = pd.read_csv("data/体检数据_sep.txt", index_col=0, sep="=")
    print(df_txt)
    # 文本能保存为 csv 也能保存为 excel
    df_txt.to_csv("data/体检数据_sep_修改.csv")
    df_txt.to_excel("data/体检数据_sep_修改.xlsx")

    print("读保存后的 csv")
    print(pd.read_csv("data/体检数据_sep_修改.csv"))

    print("读保存后的 xlsx")
    print(pd.read_excel("data/体检数据_sep_修改.xlsx"))

    # 有趣的功能：从剪切板中读数据
    df = pd.read_clipboard()
    print(df)

    # Pandas 调取解析网页当中的表格数据
    df = pd.read_html("https://mofanpy.com/tutorials/data-manipulation/pandas/read-save/")
    print(df)
    # Pandas 读数据库，读 Json 官网：https://pandas.pydata.org/docs/reference/io.html


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('从文件读取数据')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
