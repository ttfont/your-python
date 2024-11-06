# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
import pandas as pd


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press ⌘F8 to toggle the breakpoint.
    # 格式化字符
    # str.upper(); str.lower(); str.len()
    # str.strip(); str.lstrip(); str.rstrip()
    # str.split()
    # 正则方案
    # str.contains(); str.match();
    # str.replace()
    # str.extract(); str.extractall()
    # 拼接
    # str.cat()

    # 格式化字符
    py_s = "A,B,C,Aaba,Baca,CABA,dog,cat"
    print("python:\n", py_s.upper())
    print("python lower:\n", py_s.lower())
    print("python len:\n", [len(s) for s in py_s.split(",")])

    pd_s = pd.Series(
        ["A", "B", "C", "Aaba", "Baca", "CABA", "dog", "cat"],
        dtype="string")
    print("\npandas:\n", pd_s.str.upper())
    print("\npandas lower:\n", pd_s.str.lower())
    print("\npandas len:\n", pd_s.str.len())

    print()
    pd_not_s = pd.Series(
        ["A", "B", "C", "Aaba", "Baca", "CABA", "dog", "cat"],
    )
    print("pd_not_s type:", pd_not_s.dtype)
    pd_s = pd_not_s.astype("string")
    print("pd_s type:", pd_s.dtype)
    print()

    py_s = ["   jack", "jill ", "    jesse    ", "frank"]
    print("python strip:\n", [s.strip() for s in py_s])
    print("\n\npython lstrip:\n", [s.lstrip() for s in py_s])
    print("\n\npython rstrip:\n", [s.rstrip() for s in py_s])

    pd_s = pd.Series(py_s, dtype="string")
    print("\npandas strip:\n", pd_s.str.strip())
    print("\npandas lstrip:\n", pd_s.str.lstrip())
    print("\npandas rstrip:\n", pd_s.str.rstrip())

    py_s = ["a_b_c", "jill_jesse", "frank"]
    print("python split:\n", [s.split("_") for s in py_s])

    pd_s = pd.Series(py_s, dtype="string")
    print("\npandas split:\n", pd_s.str.split("_"))
    print(pd_s.str.split("_", expand=True))
    pd_df = pd.DataFrame([["a", "b"], ["C", "D"]], dtype="string")
    print(pd_df.iloc[0, :].str.upper())

    # 正则方案
    pattern = r"[0-9][a-z]"
    s = pd.Series(["1", "-i1a1-iii", "1c", "abc"], dtype="string")
    print(s.str.contains(pattern))

    s = pd.Series(["1", "1a", "11c", "abc"], dtype="string")
    pattern = r"[0-9]+?[a-z]"
    print(s.str.match(pattern))

    pattern = r"[0-9][a-z]"
    print(s.str.match(pattern))

    py_s = ["1", "1a", "21c", "abc"]
    pd_s = pd.Series(py_s, dtype="string")
    print("py_s replace '1' -> '9':\n", [s.replace("1", "9") for s in py_s])
    print("\n\npd_s replace '1' -> '9':\n", pd_s.str.replace("1", "9"))
    print("pd_s replace -> 'NUM':")
    print(pd_s.str.replace(r"[0-9]", "NUM", regex=True))

    s = pd.Series(['a1', 'b2', 'c3'])
    print(s)
    print(s.str.extract(r"([ab])(\d)"))

    s = pd.Series(['a1', 'b2', 'c3', 'a1a2'])
    print(s.str.extractall(r"([ab])(\d)"))

    # 拼接
    s1 = pd.Series(["A", "B", "C", "D"], dtype="string")
    print(s1)
    s2 = pd.Series(["1", "2", "3", "4"], dtype="string")
    print(s2)
    print(s1.str.cat(s2))
    print(s1.str.cat(s2, sep="-"))


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('文字处理')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
