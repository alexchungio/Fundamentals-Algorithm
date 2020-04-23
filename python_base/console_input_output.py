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
    try:
        lyst = []
        # for line in sys.stdin
        while True:
            line = sys.stdin.readline().strip()
            if not line:
                break
            line = list(map(int, line.split()))
            lyst.append(line)
        print(lyst)
    except Exception as e:
        print(e)
        pass

def input_fixed_line():
    """
    第一行输入行数大小
    后面依次输入对应行数据
    :return:
    """
    try:
        num_line = int(input())
        lyst = []
        for index in range(num_line):
            line = sys.stdin.readline()
            line = list(map(int, line.strip().split()))
            lyst.append(line)
        print(lyst)
    except Exception as e:
        print(e)
        pass


if __name__ == "__main__":

    input_multi_line()