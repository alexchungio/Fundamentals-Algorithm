#
# @lc app=leetcode.cn id=279 lang=python3
#
# [279] 完全平方数
#

# @lc code=start
class Solution:
    def numSquares(self, n: int) -> int:
        
        # # DP(complete backpack)
        # dp[i] represents the minimum number of perfect squares required to sum up to i.

        # dp formula description:
        # there are only two possibilities for the last step:
        # 1. Choose a perfect square number j*j, then the previous number is i - j*j.
        # 2. The previous number is i, and we do not choose any perfect square number.
        # dp[i] = min(dp[i - j*j] + 1, dp[i]) for all j such that j*j <= i.  

        # initial dp array
        # 
        dp = [float('inf')] * (n+1)
        dp[0] = 0
        
        # Compute the optimal answer for every value from 1 to n.
        for i in range(1, n+1):
            # j = 1
            
            # while j * j <= i:
            #     # dp[i] = min(dp[i], dp[i - square] + 1)
            #     dp[i] = min(dp[i - j*j] + 1, dp[i])
            #     j += 1
            for j in range(1, int(i**0.5) + 1):
                dp[i] = min(dp[i - j*j] + 1, dp[i])

        return dp[n]
            
        
# @lc code=end

