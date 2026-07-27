#
# @lc app=leetcode.cn id=141 lang=python3
#
# [141] 环形链表
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:

        # quick-slow point
        slow = head
        fast = head
        
        # Traverse the linked list until fast reaches the end.
        while fast and fast.next:
            slow = slow.next  # Move slow pointer by one step.
            fast = fast.next.next  # Move fast pointer by two steps.
            
            # If the two pointers meet, a cycle exists.
            if slow == fast:
                return True

        # If fast reaches the end, there is no cycle.  
        return False
        
        
         
        
# @lc code=end

