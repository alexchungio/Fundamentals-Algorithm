#!/usr/bin/env python
# -*- coding: utf-8 -*-
#------------------------------------------------------
# @ File       : array_stack
# @ Description:  
# @ Author     : Alex Chung
# @ Contact    : yonganzhong@outlook.com
# @ License    : Copyright (c) 2017-2018
# @ Time       : 2020/5/29 8:22
# @ Software   : PyCharm
#-------------------------------------------------------

import os
import array


"""
Stack ADT: ArrayStack

This class implements the following methods:
    S.push(e)
    S.pop()
    S.peek()
    S.is_empty()
    len(S)

This class utilizes an array-based data structure,
a list, to store its data under the hood.
It only needs to keep track of that list.

This makes it an adapter class for the list,
since it adheres to the Stack ADT but does not change
the implementation of the underlying list type.
"""


class ArrayStack(object):
    """

    """
    def __init__(self):
        self._items = []
        self._len = 0

    def __iter__(self):
        cursor = 0
        while cursor < self._len:
            yield self._items[cursor]
            cursor += 1

    def __len__(self):
        return self._len

    def __str__(self):
        return str(self._items)

    def peek(self):
        if self.is_empty() is True:
            raise KeyError("The stack is empty")
        return self._items[self._len - 1]

    def is_empty(self):
        return (self._len == 0)

    def clear(self):
        self._size = 0
        self._items = []

    def push(self, item):
        self._items.append(item)
        self._len += 1

    def pop(self):
        if self.is_empty() is True:
            raise KeyError("The stack is empty")
        else:
            old_items = self._items.pop(self._len-1)
            self._len -= 1
            return old_items


if __name__ == "__main__":
    a = ArrayStack()
    a.push(5)
    a.push(15)

    # iterate stack
    for item in a:
        print(item)

    print("Peeking: {0}".format(a.peek()))
    print("Length of stack: {0}".format(len(a)))
    print("Pop: {0}".format(a.pop()))
    print("Length of stack: {0}".format(len(a)))
    print("Pop: {0}".format(a.pop()))
    print("Length of stack: {0}".format(len(a)))



