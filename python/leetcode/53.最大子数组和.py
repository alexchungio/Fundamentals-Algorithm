#
# @lc app=leetcode.cn id=53 lang=python3
#
# [53] 最大子数组和
#

# @lc code=start
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:


        if len(nums) == 1:
            return nums[0]

        cur_sum = 0
        max_sum = float('-inf')

        for i in range(len(nums)):
            
            # add the current element to the current sum
            cur_sum += nums[i]

            # update global maximum
            max_sum = max(max_sum, cur_sum)

            # if the current subarray sum is non-positive
            # reset start index from next and reset current sum
            if cur_sum <= 0:
                cur_sum = 0

        return max_sum
                    
# @lc code=end

