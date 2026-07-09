#
# @lc app=leetcode.cn id=77 lang=python
#
# [77] 组合
#

# @lc code=start

class Solution:
    def combine(self, n: int, k: int):
        res = []
        path = []
        def backtracking(n, k, start_idx):
            if len(path) == k:
                res.append(path[:])
                return
            for i in range(start_idx, n+1):
                path.append(i)
                backtracking(n, k, i+1)
                path.pop()
                
        backtracking(n, k, 1)
        
        return res
        
# @lc code=end

