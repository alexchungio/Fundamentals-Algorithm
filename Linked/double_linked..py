#!/usr/bin/env python
# -*- coding: utf-8 -*-
#------------------------------------------------------
# @ File       : double_linked.
# @ Description:  
# @ Author     : Alex Chung
# @ Contact    : yonganzhong@outlook.com
# @ License    : Copyright (c) 2017-2018
# @ Time       : 2020/5/24 11:29
# @ Software   : PyCharm
#-------------------------------------------------------


from Linked.node import DoubleLinkedNode


def insert_head(head, item):
    """
    add node to head
    :param head:
    :param item:
    :return:
    """
    if head is None:
        head = DoubleLinkedNode(item)
    else:
        head = DoubleLinkedNode(item, next=head)
        head.next.prev = head

    return head


def insert_tail(head, item):
    """
    add data to tail
    :param data:
    :param linked:
    :return:
    """
    probe = head
    if head is None:
        head = DoubleLinkedNode(item)
    else:
        # traversal to linked tail
        while probe.next != None:
            probe = probe.next
        # insert data to tail
        probe.next = DoubleLinkedNode(item, prev=probe)
    return head


def traversal_linked(head, is_reverse=False):
    """
    traversal linked list
    :param head:
    :param is_reverse: is or not to traversal by reverse
    :return:
    """
    probe = head
    if head is None:
        pass
    if is_reverse:
        # probe to tail of linked list
        while probe.next != None:
            probe = probe.next
        # reverse traversal
        while probe != None:
            print(probe.data)
            probe = probe.prev
    else:
        while probe != None:
            print(probe.data)
            probe = probe.next


if __name__ == "__main__":
    head = None

    for i in range(6):
        # head = insert_head(head, i)
        head = insert_tail(head, i)

    print('traversal linked list')
    traversal_linked(head)
    print('traversal by reverse')
    traversal_linked(head, is_reverse=True)


