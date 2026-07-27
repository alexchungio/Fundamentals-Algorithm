#
# @lc app=leetcode.cn id=104 lang=python3
#
# [104] 二叉树的最大深度
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        
        # height(leaf -> root): post-traversal   
        def dfs_post(cur_node):
            
            if cur_node is None:
                return 0
            
            left_height = dfs_post(cur_node.left)
            right_height = dfs_post(cur_node.right)

            # update node height
            height =  max(left_height, right_height) + 1

            return height
        
        ans = dfs_post(root)

        return ans


        # depth(root -> leaf) -> pre-traversal

        # max_depth = 0
        # def dfs_pre(cur_node, cur_depth):
            
        #     if cur_node is None:
        #         return
            
        #     nonlocal max_depth
        #     max_depth = max(max_depth, cur_depth)

        #     dfs_pre(cur_node.left, cur_depth+1) 
        #     dfs_pre(cur_node.right, cur_depth+1) 
        
        # dfs_pre(root, 1)

        # return max_depth
            
   
# @lc code=end

