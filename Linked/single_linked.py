# @Time 2020/05/01 17:44
# @Author AlexChung

import os

from Linked.node import Node


def insert_head(head:Node, item):
    """
    add node to head
    :param data:
    :param linked:
    :return:
    """
    # if head is None:
    #     head = Node(data, head)
    # else:
    #     head = Node(data, head)

    # Note: default format equal to head insert
    head = Node(item, head)
    return head


def insert_tail(head:Node, item):
    """

    :param data:
    :param linked:
    :return:
    """
    probe = head
    if head is None:
        head = Node(item)
    else:
        # traversal to linked tail
        while probe.next != None:
            probe = probe.next
        # insert data to tail
        probe.next = Node(item)
    return head


def delete_head(head:Node):
    """
    delete from head
    :param head:
    :return:
    """
    # only one node
    # if head.next is None:
    #     head = Node
    # else:
    #     head = head.next
    # assert linked list is not None
    assert head is not None
    head = head.next
    return head


def delete_tail(head:Node):
    """
    delete from tail
    :param head:
    :return:
    """
    # assert linked list is not None
    assert head is not None

    # only one node
    probe = head
    if probe.next is None:
        head = None
    # has at least two node
    else:
        # curse to the second to last node
        if probe.next.next is not None:
            probe = probe.next
        # set the second to last Node point to None equal to remove first to last Node
        probe.next = None

    return head


def insert(head:Node, index, item):
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
        head = Node(item, head)

    else:
        probe = head
        # curse to position of index-1
        # or the last position
        while index > 1 and probe.next != None:
            probe = probe.next
            index -= 1
        # insert new node after node at position index-1
        probe.next = Node(item, probe.next)

    return head


def delete(head:Node, index):
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
    else:
        probe = head
        # curse to position of index-1
        # or the next to last position
        while index > 1 and probe.next.next != None:
            probe = probe.next
            index -= 1
        probe.next = probe.next.next

    return head


def traversal_linked(head:Node):
    """
    traversal linked list
    :param head:
    :return:
    """
    probe = head
    while probe != None:
        print(probe.data)
        probe = probe.next


if __name__ == "__main__":
    print("construct one node linked")
    head = Node(0)
    traversal_linked(head)

    print("add one node to the head of linked")
    head = insert_head(head, 1)
    traversal_linked(head)

    print("add one node to the tail of linked")
    head = insert_tail(head, 2)
    traversal_linked(head)

    print("add one node to the any index of linked")
    head = insert(head, 2, -1)
    traversal_linked(head)

    print("delete one node from any index of linked")
    head = delete(head, 2)
    traversal_linked(head)

    print("delete one node from the head of linked")
    head = delete_head(head)
    traversal_linked(head)

    print("delete one node from the tail of linked")
    head = delete_tail(head)
    traversal_linked(head)







