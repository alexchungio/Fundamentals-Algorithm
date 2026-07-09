#
# @lc app=leetcode id=1 lang=python
#
# [1] Two Sum
#

# @lc code=start
class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        res = []
        num_map = {}
        
        for idx, num in enumerate(nums):
            if target - num in num_map:
                return [num_map[target - num], idx]
            
            num_map[num] = idx
        
# @lc code=end

