#
# @lc app=leetcode.cn id=160 lang=python3
#
# [160] 相交链表
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        

        if headA == None or headB == None:
            return None
        
        # tow points
        dummy_a = headA  # max step -> a + b + c
        dummy_b = headB  # max step -> a + b + c

        while(dummy_a != dummy_b):
            
            dummy_a = dummy_a.next if dummy_a else headB
            dummy_b = dummy_b.next if dummy_b else headA

        return dummy_a  # intersection val 
     
        
# @lc code=end

