#
# @lc app=leetcode.cn id=145 lang=python3
#
# [145] 二叉树的后序遍历
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:

        vec = []
        def dfs_post(cur_node: Optional[TreeNode]):
            if cur_node is None:
                return
            dfs_post(cur_node.left)
            dfs_post(cur_node.right)
            vec.append(cur_node.val)

        dfs_post(root)
        return vec
        
# @lc code=end

