# @Time 2020/05/01 16:30
# @Author AlexChung


from Linked.node import Node
from Linked.single_linked import insert_tail, traversal_linked

def local_reversal(head:Node):
    """
    就地反转
    1->2->3->4->5
    反转过程
    dummy->2->1->3->4->5
    dummy->3->2->1->4->5
    dummy->4>-3->2->1->5
    dummy->5->4->3->2->1

    # 需要三个指针
    dummy: 用于指向新链表的头节点
    p_pre: 用于指向待反转节点的前一个节点，目的是为了记录反转操作位置
    p_cur: 当前待反转节点
    :param head:
    :return:
    """

    # step 1 initial node
    dummy = Node(-1)
    dummy.next = head
    p_pre = head
    p_cur = p_pre.next

    # step 2 one node condition
    if p_pre is None or p_cur is None:
        return head
    # step 3
    else:
        # loop condition
        while p_cur != None:
            # step 3.1 update p_pre loop position
            # after this step, we can operation p_cur, equal to separate p_cur to linked
            p_pre.next = p_cur.next
            # step 3.2 insert current to the head of new linked
            # note the dummy pointer to the head of new linked , not the new linked head
            p_cur.next = dummy.next
            # step 3.3 update dummy status to new head of linked
            # now the new linked head is p_cur
            dummy.next = p_cur
            # recover p_cur to the next node of p_pre for next iteration
            p_cur = p_pre.next

        head = dummy.next

    return head


def insert_reversal(head:Node):
    """
    头节点插入法（需新建链表）
    :param head:
    :return:
    """
    pass


if __name__ == "__main__":
    # create linked list
    head = Node(1)
    for i in range(2, 6):
        head = insert_tail(head, i)
    traversal_linked(head)

    # reverse linked
    print("local reverse result")
    head = local_reversal(head)
    traversal_linked(head)