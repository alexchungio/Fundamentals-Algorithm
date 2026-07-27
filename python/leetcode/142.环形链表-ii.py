#
# @lc app=leetcode.cn id=142 lang=python3
#
# [142] 环形链表 II
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:

        slow = head
        fast = head
        
        # check whether a cycle exists.
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

            # The two pointers meet inside the cycle.
            if slow == fast:
                # Let:
                # a = distance from the head to the cycle entrance.
                # b = distance from the cycle entrance to the meeting point.
                # c = distance from the meeting point back to the cycle entrance.
                # Since fast moves twice as fast as slow:
                #   2(a + b) = a + b + k(b + c)
                # Simplify:
                #   a + b = k(b + c)
                #   a = (k - 1)(b + c) + c
                while slow is not head:
                    head = head.next
                    slow = slow.next  

                # Return the entrance of the cycle.
                return head
            
        # No cycle exists.  
        return None
                
        
# @lc code=end

