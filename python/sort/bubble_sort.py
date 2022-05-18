# @Time 2020/04/19 17:32
# @Author AlexChung
# Time Complexity O(n**2)

def swap(lyst, m, n):
    """
    交换list元素
    :param n:i
    :param m:
    :return:
    """
    lyst[m], lyst[n] = lyst[n], lyst[m]


def bubble_sort(lyst):
    """
    冒泡排序（稳定）
    :param lyst:
    :return:
    """
    step = 0
    for n in range(len(lyst), 0, -1):
        for m in range(1, n):
            step += 1
            if lyst[m] < lyst[m-1]:
                swap(lyst, m, m-1)
    print('Time step: {0}'.format(step))
    return lyst


def bubble_sort_early_terminal(lyst):
    """
    提前终止的冒泡排序
    :param lyst:
    :return:
    """
    step = 0
    for n in range(len(lyst), 0, -1):
        sorted_flag = False  # the rest is or not sorted
        for m in range(1, n):
            step += 1
            sorted_flag = True
            if lyst[m] < lyst[m - 1]:
                swap(lyst, m, m - 1)
                sorted_flag = False  # update sorted flag to False
        if sorted_flag is True:
            break
    print('Time step: {0}'.format(step))
    return lyst


if __name__ == "__main__":
    lyst = [1, 2, 3, 6, 5, 8, 10, 4, 9]
    print(bubble_sort(lyst))

    print(bubble_sort_early_terminal(lyst))