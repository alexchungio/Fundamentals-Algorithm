#
# @lc app=leetcode.cn id=21 lang=python3
#
# [21] 合并两个有序链表
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:

        if list1 is None:
            return list2

        if list2 is None:
            return list1
        
        # dummy node to simplify edge cases
        dummy_node = ListNode(None)
        merge_list = dummy_node

        # attach the remaining non-empty list
        while list1 and list2:
           
            if list1.val <= list2.val:
                dummy_node.next = list1
                dummy_node = list1
                list1  = list1.next 
            else:
                dummy_node.next = list2
                dummy_node = list2
                list2 = list2.next

        # attach the remaining non-empty list
        dummy_node.next = list1 if list1 else list2

        return merge_list.next
                  
        
# @lc code=end

