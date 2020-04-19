# @Time 2020/04/15 20:12
# @Author AlexChung


import os


def swap(lyst, m, n):
    """
    交换list元素
    :param n:i
    :param m:
    :return:
    """
    lyst[m], lyst[n] = lyst[n], lyst[m]


def displacement(lyst, m, n):

    """
    移动 list 元素位置 同时保持其他元素相对位置不变
    :param lyst:
    :param m:
    :param n:
    :return:
    """
    v = lyst[n]
    lyst.pop(n)
    lyst.insert(m, v)


def custom_displacement(lyst, m, n):
    """
    移动 list 元素位置 同时保持其他元素相对位置不变
    :param lyst:
    :param m:
    :param n:
    :return:
    """
    v = lyst[n]
    # move index between (m, n-1) to (m+1, n)
    for i in range(n, m, -1):
        lyst[i] = lyst[i-1]
    lyst[m] = v


def select_sort(lyst):
    """
    选择排序（不稳定）
    交换元素
    :param lyst:
    :return:
    """

    for i in range(len(lyst) - 1):
        min_index = i
        for j in range(i+1, len(lyst)):
            if lyst[j] < lyst[min_index]:
                min_index = j
        swap(lyst, i, min_index)

    return lyst


def select_sort_early_terminal(disorder_list):
    """
    判断后面序列是否有序，提前终止排序
    :param disorder_list:
    :return:
    """
    pass


def stable_select_sort(lyst):
    """
    选择排序（稳定）
    不交换元素
    :param lyst:
    :return:
    """
    for i in range(len(lyst) - 1):
        min_index = i
        for j in range(i+1, len(lyst)):
            if lyst[j] < lyst[min_index]:
                min_index = j
        custom_displacement(lyst, i, min_index)
    return lyst


if __name__ == "__main__":
    # input_data = input("Enter numbers separated by a comma:\n").strip()
    # unsorted = [int(item) for item in input_data.split(",")]
    l = [6, 1, 2, 5, 3, 4, 8, 9, 10]
    print(stable_select_sort(l))








