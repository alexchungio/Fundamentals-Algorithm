#
# @lc app=leetcode.cn id=189 lang=python3
#
# [189] 轮转数组
#

# @lc code=start
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        # reverse all list
        self.reverse(nums, 0, len(nums) - 1)

        k = k % len(nums)

        # reverse sub-0
        self.reverse(nums, 0, k-1)
        # reverse sub-1
        self.reverse(nums, k, len(nums) -1)

        return nums

        
    def reverse(self, nums, start, end):
        
        while start < end:
            tmp = nums[start]
            nums[start] = nums[end]
            nums[end] = tmp
            start += 1
            end -= 1

            
        
# @lc code=end

