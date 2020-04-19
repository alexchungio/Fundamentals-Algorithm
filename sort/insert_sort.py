# @Time 2020/04/19 20:30
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


def insert_sort(lyst):
    """
    插入排序
    :param lyst:
    :return:
    """
    step = 0
    for i in range(1, len(lyst)):
        j = i - 1
        while j >= 0:
            step += 1
            if lyst[j] > lyst[j + 1]:
                swap(lyst, j, j+1)
            else:
                break
            j -= 1
    print(step)
    return lyst

if __name__ == "__main__":

    lyst = [1, 2, 3, 6, 5, 10, 4, 9]
    print(insert_sort(lyst))




