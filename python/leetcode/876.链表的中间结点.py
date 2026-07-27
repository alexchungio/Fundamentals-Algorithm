#
# @lc app=leetcode.cn id=876 lang=python3
#
# [876] 链表的中间结点
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:

        # Move the fast pointer two steps and the slow pointer one step.

        # Odd-length list:
        # fast stops at the last node, and slow points to the middle node.
        
        # Even-length list:
        # fast becomes None after moving past the last node,
        # and slow points to the second middle node,

        slow = head
        fast = head

        # When the fast pointer reaches the end,
        # the slow pointer will be at the middle node.
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next  

        # Return the middle node.
        # If the list has two middle nodes, the second one is returned.
        return slow
        
# @lc code=end

