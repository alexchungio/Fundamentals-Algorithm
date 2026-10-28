#
# @lc app=leetcode.cn id=746 lang=python3
#
# [746] 使用最小花费爬楼梯
#

# @lc code=start
class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:


        # dp formula description:
        # there are only two possibilities for the last step:
        # 1. Climb 1 step from step i - 1.
        # 2. Climb 2 steps from step i - 2.
        # dp[i] = min(dp[i-1] + cost[i-1], dp[i-2]+cost[i-2])
        
        # create dp array
        # dp[*]: number of climb method
        dp = [0] * 2

        # initial boundary
        dp[0] = 0
        dp[1] = 0
        
        # [1, 2, ..., n]
        for i in range(2, len(cost) + 1):
            # dp[i] = min(dp[i-1] + cost[i-1], dp[i-2]+cost[i-2])
            dp_i = min(dp[1] + cost[i-1], dp[0] + cost[i-2])
            dp[0] = dp[1]
            dp[1] = dp_i

        return dp[1]  
        
# @lc code=end

