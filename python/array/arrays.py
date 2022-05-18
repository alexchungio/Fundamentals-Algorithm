# @Time 2020/04/29 08:29
# @Author AlexChung

"""
custom array
the fill value is None by default
"""

class Array(object):

    def __init__(self, capacity, fill_value=None):
        self._items = list()
        for index in range(capacity):
            self._items.append(fill_value)

    def __len__(self):
        return len(self._items)

    def __str__(self):
        return str(self._items)

    def __iter__(self):
        return iter(self._items)

    def __getitem__(self, index):
        return self._items[index]

    def __setitem__(self, index, value):
        self._items[index] = value


if __name__ == "__main__":
    a = Array(10, 1)
    print(len(a))

    # traverse array and set value
    for index in range(len(a)):
        a[index] = a[index] + index

    # traverse array and print
    for item in a:
        print(item)
