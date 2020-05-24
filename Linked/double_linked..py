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


def insert(head, index, item):
    """
    insert anywhere of index
    if index low 0 then insert to head(0 index)
    if index out of range index of linked then insert to tail

    :param head:
    :param index:
    :param value:
    :return:
    """
    # insert to head
    if head is None or index <= 0:
        head = DoubleLinkedNode(item, next=head)
        head.next.prev = head
    else:
        probe = head
        # curse to position of index-1
        # or the last position
        while index > 1 and probe.next != None:
            probe = probe.next
            index -= 1
        # insert new node after node at position index-1
        probe.next = DoubleLinkedNode(item, prev=probe, next=probe.next)

    return head


def delete(head, index):
    """
    delete anywhere of index
    if index low 0 then insert to head(0 index)
    if index out of range index of linked then insert to tail
    :param head:
    :param index:
    :param item:
    :return:
    """
    assert head is not None
    if index <= 0:
        head = head.next
        head.prev = None
    else:
        probe = head
        # curse to position of index-1
        # or the next to last position
        while index > 1 and probe.next.next != None:
            probe = probe.next
            index -= 1
        probe.next = probe.next.next
        probe.next.prev = probe

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

    print('The inserted index is beyond the chain table boundary')
    head = insert(head, item='a', index=-1)
    traversal_linked(head)
    print('The inserted index is inner the chain table boundary')
    head = insert(head, item='b', index=2)
    traversal_linked(head)

    print('The delete index is beyond the chain table boundary ')
    head = delete(head, index=-1)
    traversal_linked(head)
    print('The delete index is inner the chain table boundary')
    head = delete(head, index=1)
    traversal_linked(head)

