#
# @lc app=leetcode.cn id=283 lang=python3
#
# [283] 移动零
#

# @lc code=start
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        slow = 0
        for fast in range(len(nums)):
            if(nums[fast] != 0):
                nums = self.swap(nums, slow, fast)
                slow += 1
                
        return nums
    
    def swap(self, nums, x, y):
        tmp = nums[x]
        nums[x] = nums[y]
        nums[y] = tmp

        return nums
            
        
# @lc code=end

