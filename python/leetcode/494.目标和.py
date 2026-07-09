#
# @lc app=leetcode.cn id=494 lang=python3
#
# [494] 目标和
#

# @lc code=start
class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        
        # dp -> 01 backpack
        
        # p -> positive, n -> negtive
        # p - n = target
        # p + n = sum
        # p = (target + sum) / 2

        num_sum = sum(nums)

        if abs(target) > num_sum:
            return 0
        
        if (target + num_sum) % 2:
            return 0
        
        bag_size = (target + num_sum) // 2
        # dp equation -> dp[j] += dp[j - nums[i]]
        # creat dp
        dp = [0] * (bag_size + 1)

        # initial boundary
        dp[0] = 1

        for i in range(len(nums)):
            # reverse order to ensure that each number is used only once
            for j in range(bag_size, nums[i]-1, -1):
                dp[j] += dp[j - nums[i]]

        return dp[bag_size]
                   
# @lc code=end

