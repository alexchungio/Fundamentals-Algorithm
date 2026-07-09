#
# @lc app=leetcode.cn id=78 lang=python3
#
# [78] 子集
#

# @lc code=start
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:

        res = [[]]
        path = []
        def backtracking(nums, start_idx):
            # no stop condition

            nonlocal path
            for i in range(start_idx, len(nums)):
                
                path.append(nums[i])
                res.append(path[:])
                backtracking(nums, i+1)
                path.pop()
                
        backtracking(nums, 0)

        return res
        
# @lc code=end

