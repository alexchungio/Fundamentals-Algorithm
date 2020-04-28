# @Time 2020/04/28 08:03
# @Author AlexChung
# Time Complexity O(n**2)


def swap(lyst, m, n):
    tmp = lyst[m]
    lyst[m] = lyst[n]
    lyst[n] = tmp


def quick_sort(lyst):
    """
    quick sort
    :param lyst:
    :return:
    """
    quick_sort_recursion_module(lyst, 0, len(lyst)-1)


def quick_sort_recursion_module(lyst, left, right):
    """

    :param lyst:
    :param left:
    :param right:
    :return:
    """
    if left < right:
        pivot_location = partition(lyst, left, right)
        quick_sort_recursion_module(lyst, left, pivot_location - 1)
        quick_sort_recursion_module(lyst, right, pivot_location + 1)


def partition(lyst, left, right):
    """

    :param lyst:
    :param left:
    :param right:
    :return:
    """
    middle_index = (left + right) // 2
    num_pivot = lyst[middle_index]
    # swap pivot with last item
    swap(lyst, middle_index, right)
    # record boundary
    boundary = left
    for index in range(left, right):
        if lyst[index] < num_pivot:
            swap(lyst, index, boundary)
            boundary += 1
    # swap pivot to boundary
    swap(lyst, right, boundary)

    return boundary





if __name__ == "__main__":
    pass