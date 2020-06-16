#!/usr/bin/env python
# -*- coding: utf-8 -*-
#------------------------------------------------------
# @ File       : linked_stack
# @ Description:  
# @ Author     : Alex Chung
# @ Contact    : yonganzhong@outlook.com
# @ License    : Copyright (c) 2017-2018
# @ Time       : 2020/5/29 10:30
# @ Software   : PyCharm
#-------------------------------------------------------


class Node(object):
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

class LinkedStack(object):
    """

    """
    def __init__(self):
        self._items = None
        self._size = 0

    def __len__(self):
        return self._size

    def __iter__(self):
        """
        visit items from bottom to top of stack
        :return:
        """
        tmp_list = list()

        def visit_node(node):
            if node is not None:
                visit_node(node.next)
                tmp_list.append(node.data)
        visit_node(self._items)
        return iter(tmp_list)

    def is_empty(self):
        return (self._size == 0)

    def peek(self):
        if self.is_empty():
            raise KeyError("The stack is empty")
        return self._items.data

    def clear(self):
        self._items = None
        self._size = 0

    def push(self, item):
        """
        insert item to top of stack
        :param item:
        :return:
        """
        self._items = Node(item, self._items)
        self._size += 1

    def pop(self):
        """
        remove and return the items at top of stack
        :return:
        """
        if self.is_empty():
            raise KeyError("The stack is Empty")
        else:
            old_item = self._items
            self._items = self._items.next
            self._size -= 1
            return old_item.data


if __name__ == "__main__":

    a = LinkedStack()
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

