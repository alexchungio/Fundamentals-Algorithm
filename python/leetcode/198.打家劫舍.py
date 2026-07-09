#
# @lc app=leetcode.cn id=198 lang=python3
#
# [198] 打家劫舍
#

# @lc code=start
class Solution:
    def rob(self, nums: List[int]) -> int:
        
        # 
        # store the number of adjacent dp 
        # inital with 0
        dp = [0] * 2  

        for i, n in enumerate(nums):
            # dp equation: dp[n] = max(dp[n-2]+nums[n], dp[n-1])
            dp_i = max(dp[0]+ n, dp[1])
            # update dp
            dp[0] = dp[1]
            dp[1] = dp_i
                
        return dp[1]  
# @lc code=end

