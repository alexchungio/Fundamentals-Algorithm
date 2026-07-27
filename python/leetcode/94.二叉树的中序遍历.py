#
# @lc app=leetcode.cn id=94 lang=python3
#
# [94] 二叉树的中序遍历
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
           
        vec = []
        def dfs_mid(cur_node: Optional[TreeNode]):
            if cur_node is None:
                return
            dfs_mid(cur_node.left)
            vec.append(cur_node.val)
            dfs_mid(cur_node.right)


        dfs_mid(root)
        return vec
# @lc code=end

