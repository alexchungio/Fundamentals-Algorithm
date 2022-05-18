# @Time 2020/05/01 17:42
# @Author AlexChung

import os


class Node(object):
    def __init__(self, data, next=None):
        self.data = data
        self.next = next


class DoubleLinkedNode(object):
    def __init__(self, data, prev=None, next=None):
        self.data = data
        self.prev = prev
        self.next = next
