#
# @lc app=leetcode.cn id=543 lang=python3
#
# [543] 二叉树的直径
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:

        # Base case: null node has height 0
        if not root:
            return 0

        ans = 0
        def dfs_post(cur_node):
            
            if cur_node is None:
                return 0
            
            left_height = dfs_post(cur_node.left)
            right_height = dfs_post(cur_node.right)

            # Update longest path that passes through this node
            nonlocal ans
            ans = max(ans, left_height + right_height)

            # Return the height of this subtree: longer child height + 1 edge to this node
            return max(left_height, right_height) + 1
        
        dfs_post(root)

        return ans
                  
        
# @lc code=end

