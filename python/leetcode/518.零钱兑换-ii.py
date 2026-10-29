#
# @lc app=leetcode.cn id=518 lang=python3
#
# [518] 零钱兑换 II
#

# @lc code=start
class Solution:
    def change(self, amount: int, coins: list[int]) -> int:

        # compare backpack problem 
        # backpack problem: dp[i] = dp[i] + dp[i - c]

        # dp formula description:
        # there are only two possibilities for the last step:
        # 1. Do not use the current coin, then the previous amount is m.
        # 2. Use one more current coin, then the previous amount is m - c
        # dp[m] = dp[m] + dp[m - c]

        dp = [0] * (amount + 1)
        dp[0] = 1

        for c in coins:
            for m in range(c, amount + 1):
                dp[m] += dp[m - c]
    
        ans = dp[amount]

        return ans  
# @lc code=end

