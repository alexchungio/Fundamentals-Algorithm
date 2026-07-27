#
# @lc app=leetcode.cn id=111 lang=python3
#
# [111] 二叉树的最小深度
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:

        if not root:
            return 0
        
        # post-traversal
        def dfs_post(cur_node):
            
            # empty node should be ignored and return infinity
            if cur_node is None:
                return float('inf')
            
            # depth of leaf node equal to 1
            if cur_node and cur_node.left is None and cur_node.right is None:
                return 1
            
            height_left = dfs_post(cur_node.left)
            height_right = dfs_post(cur_node.right)

            height = min(height_left, height_right) + 1

            return height

        ans = dfs_post(root)

        return ans 
        
# @lc code=end

