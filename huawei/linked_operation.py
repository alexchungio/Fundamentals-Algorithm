import os


class Node(object):
    def __init__(self, data, next=None):
        self.data = data
        self.next = next


def add(link: Node, value):

    head_link = link
    while True:
        if link.next is not None:
            link = link.next
            continue
        else:
            link.next = Node(value)
            break
    return head_link


def delete():
    pass


def insert():
    pass


def traversal_link(link):
    probe = link
    while True:
        try:
            if probe is not None:
                print(probe.data)
                probe = probe.next
            else:
                break
        except Exception as e:
            print(e)
            break


if __name__ == "__main__":

    link = Node(1)
    link = add(link, 2)
    link = add(link, 3)

    traversal_link(link)
