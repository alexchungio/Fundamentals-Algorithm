#
# @lc app=leetcode.cn id=300 lang=python3
#
# [300] 最长递增子序列
#

# @lc code=start
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:

        # Linear DP

        n = len(nums)
        if n <= 1:
            return n
        # Store the maximum LIS length
        result = 1

        # initial dp array
        dp = [1] * len(nums)

        for i in range(1, n):
            for j in range(i):
                # If nums[i] can extend the increasing subsequence ending at nums[j]
                if(nums[i] > nums[j]):
                    # # dp[i] = max(dp[i], dp[j] + 1)
                    dp[i] = max(dp[i], dp[j] + 1)

                # update global max result
                result = max(result, dp[i])

        return result
        
        
# @lc code=end

