# @Time 2020/05/01 17:44
# @Author AlexChung

import os

from Linked.node import Node


def add_head(data, linked:Node):
    """
    add node to head
    :param data:
    :param linked:
    :return:
    """
    if linked is None:
        head = Node(data)
    else:
        head = Node(data, linked)
    return head


def add_tail(data, head:Node):
    """

    :param data:
    :param linked:
    :return:
    """
    probe = head
    if head is None:
        head = Node(data)
    else:
        # traversal to linked tail
        while probe.next != None:
            probe = probe.next
        # insert data to tail
        probe.next = Node(data)
    return head


def traversal_linked(head:Node):
    """

    :param head:
    :return:
    """
    probe = head

    while probe != None:
        print(probe.data)
        probe = probe.next


if __name__ == "__main__":
    head = Node(0)
    traversal_linked(head)

    head = add_head(1, head)
    traversal_linked(head)

    head = add_tail(2, head)
    traversal_linked(head)

