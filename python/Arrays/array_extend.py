from Arrays.arrays import Array

capacity_size = 5  # physical size
logical_size = 0  # logical size


def resize(a: Array, max):
    """
    resize array
    :param a:
    :param max:
    :return:
    """
    tmp = Array(max)
    for i in range(logical_size):
        tmp[i] = a[i]
    a = tmp
    return a


def extend_array(a: Array):
    """
    reduce array
    :param a:
    :return:
    """
    if logical_size == len(a):
        a = resize(a, max=2 * len(a))

    return a


def reduce_array(a: Array):
    """
    reduce array
    :param a:
    :return:
    """
    if logical_size <= len(a) // 4 and len(a) >= capacity_size * 2:
        resize(a, max=len(a) // 2)
    return a


def insert(a, target_index, item):
    """
    insert value to array
    :param a:
    :param target_index:
    :param value:
    :param logical_size:
    :return:
    """
    global logical_size
    # step 1 check array is full
    # increase physical size of array if necessary
    if logical_size == len(a):
        a = resize(a, max=2 * len(a))

    # step 2 shift element down
    for i in range(logical_size, target_index, -1):
        a[i + 1] = a[i]

    # step 3 add the item and increment logical size
    a[target_index] = item
    logical_size += 1

    return a


def delete(a: Array, target_index):
    """

    :param a:
    :param target_index:
    :return:
    """
    global logical_size
    # step 1 shift items up
    for i in range(target_index, logical_size - 1):
        a[i] = a[i + 1]
    # step 2 decrement logical size
    logical_size -= 1
    # decrease size fo array if necessary
    # logical_size <= len(a) // 4 保证压缩物理空间后，物理空间压缩一半后，物理空间为逻辑空间的2倍
    # len(a) >= capacity_size * 2 保证物理空间至少为容量空间（最小单位）的2倍，才能继续执行压缩
    if logical_size <= len(a) // 4 and len(a) >= capacity_size * 2:
        a = resize(a, len(a) // 2)
    return a


if __name__ == "__main__":

    a = Array(capacity=capacity_size)

    # test insert
    for i in range(20):
        a = insert(a, i, i)
        print("step {0}:  logical size {1} physical size {2}: ".format(i, logical_size, len(a)))

    # test delete
    for i in range(logical_size):
        a = delete(a, 0)
        print("step {0}:  logical size {1} physical size {2}: ".format(i, logical_size, len(a)))










