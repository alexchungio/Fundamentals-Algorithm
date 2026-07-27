#
# @lc app=leetcode.cn id=102 lang=python3
#
# [102] 二叉树的层序遍历
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        # base case
        if not root:
            return []

        ans = []
        # Queue for BFS, storing nodes of current/next leve
        queue = collections.deque()

        # Start with the root node
        queue.append(root)

        while queue:
            #  Number of nodes at the current level
            size = len(queue) 
            # store node val at the current level
            vec = []  
            # Process all nodes of the current level
            for _ in range(size):
                #  Dequeue the front node
                node = queue.popleft()
                vec.append(node.val)
                
                if node.left is not None:
                    queue.append(node.left)
                if node.right is not None:
                    queue.append(node.right)

            # append result at current level
            ans.append(vec)

        return ans      
        
# @lc code=end

