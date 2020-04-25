import sys


def input_single_line():
    """
    读取一行,
    这里假设输入为两个数字
    :return:
    """
    m, n = map(int, sys.stdin.readline().strip().split())
    print(m, n)


def input_multi_line():
    """
    输入多行数据
    :return:
    """
    while True:
        try:
            lyst = []
            # for line in sys.stdin
            while True:
                line = sys.stdin.readline().strip()
                # if line == ''
                if not line:
                    break
                line = list(map(int, line.split()))
                lyst.append(line)
            print(lyst)
        except Exception as e:
            break


def input_fixed_line():
    """
    第一行输入行数大小
    后面依次输入对应行数据
    :return:
    """
    while True:
        try:
            num_line = int(input())
            lyst = []
            for index in range(num_line):
                line = sys.stdin.readline()
                line = list(map(int, line.strip().split()))
                lyst.append(line)
            print(lyst)
        except Exception as e:
            break


def compare_input_readline():
    """
    input 只读取字符串，自动去掉换行符(\n)
    readline: 读取整行信息，包括换行符(\n)

    :return:
    """
    m = input()
    n = sys.stdin.readline()
    print(len(m))
    print(len(n))
    assert m == n.strip(), "m != n"


def strip_test():
    """
    strip: 移除字符串头尾指定的字符，当chars==None时，移除首尾的 ’ ‘|’\n‘|’\t‘
           Note: 只能删除首位，不能删除中间数据
    :return:
    """
    m = "good"
    n = " good\n"
    q = "good\t\n"

    # print raw length
    print("Now print raw length")
    print(len(m))
    print(len(n))
    print(len(q))

    # execute strip
    n = n.strip()
    q = n.strip()

    assert m == n and n == q, "m, n, q"
    # print update length
    print('Following print length by strip')
    print(len(m))
    print(len(n))
    print(len(q))


if __name__ == "__main__":

    # compare_input_readline()
    # m = " falgafab\n\t"
    # print(len(m))
    # print(len(m.strip()))
    strip_test()