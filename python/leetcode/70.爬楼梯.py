#
# @lc app=leetcode.cn id=70 lang=python3
#
# [70] 爬楼梯
#

# @lc code=start
class Solution:
    def climbStairs(self, n: int) -> int:
        
        if n == 1:
            return 1
        
        # create dp array
        # dp[*]: number of climb method
        dp = [1] * 2

        # initial boundary
        dp[0] = 1
        dp[1] = 2

        for i in range(3, n+1):
            # dp[n] = dp[n-1] + dp[n-2]
            sum = dp[0]+ dp[1]
            dp[0] = dp[1]
            dp[1] = sum

        return dp[1]    
        
        
# @lc code=end

