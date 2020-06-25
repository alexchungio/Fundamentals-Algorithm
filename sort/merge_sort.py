# @Time 2020/04/28 08:41
# @Author AlexChung
# Time Complexity O(nlog2(n))


def merge_sort(lyst):
    """

    :param lyst:
    :return:
    """
    merge_sort_help(lyst, 0, len(lyst) -1)

    return lyst


def merge_sort_help(lyst, low, high):
    """

    :param lyst:
    :param low:
    :param high:
    :return:
    """
    if low < high:
        middle = (low + high) // 2
        merge_sort_help(lyst, low, middle)
        merge_sort_help(lyst, middle+1, high)
        merge(lyst, low, middle, high)


def merge(lyst, low, middle, high):
    """
    merge 两个排序好的子列表，合并到一个大的排序列表
    :param lyst:
    :param low:
    :param middle:
    :param high:
    :return:
    """
    copy_buffer = [0] * len(lyst)
    print(copy_buffer)
    print(low, high)
    left_index = low
    right_index = middle + 1

    for i in range(low, high+1):
        # left exhausted
        if left_index > middle:
            copy_buffer[i] = lyst[right_index]
            right_index += 1
        elif right_index > high:
            copy_buffer[i] = lyst[left_index]
            left_index += 1
        elif lyst[left_index] < lyst[right_index]:
            print(i, left_index)
            copy_buffer[i] = lyst[left_index]
            left_index += 1
        else:
            copy_buffer[i] = lyst[right_index]
            right_index += 1

    # copy sorted item back to proper position in lyst
    lyst[low: high+1] = copy_buffer[low: high+1]


if __name__ == "__main__":
     lyst = [1, 2, 7, 8, 6, 5, 10, 4, 9]
     merge_sort(lyst)
     print(lyst)
