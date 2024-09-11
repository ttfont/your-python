# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press ⌘F8 to toggle the breakpoint.
    # for 循环
    for i in range(5):
        print("新文件-" + str(i))
    print()
    for i in range(2, 5):
        print("新文件-" + str(i))
    print()
    for i in range(3, 10, 2):
        print("新文件-" + str(i))
    print()
    # While 循环
    # for	天然适合在有限的循环中
    # while	可以被用在无限循环中
    guess_num = 10
    while guess_num != 20:
        guess_num += 1
        print(guess_num)
    print()
    # continue 和 break
    count = 0
    guess_num = 30
    while guess_num != 20 and count <= 10:
        guess_num -= 1
        count += 1
        print(guess_num)
    print()

    count = 0
    guess_num = 10
    while guess_num != 20:
        guess_num += 1
        count += 1
        if count > 10:
            break
        print(guess_num)
    print()
    for i in range(10):
        if i == 5:
            break
        print(i)
    print()
    for i in range(10):
        if i % 2 == 0:
            continue  # 跳过偶数
        print(i)
    # break	中止循环
    # continue 跳出当前循环，进行下一个循环


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('for 和 while 循环')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
