#
# @lc app=leetcode.cn id=322 lang=python3
#
# [322] 零钱兑换
#

# @lc code=start
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:

        
        # Greedy algorithm incorrect
        # DP(complete backpack)

        # dp formula description:
        # dp[i] stores the minimum number of coins needed to form amount i.
        # there are only two possibilities for the last step:
        # 1. Do not use the current coin, then the previous amount is m.
        # 2. Use one more current coin, then the previous amount is m - c
        # dp[m] = min(dp[m], dp[m-c]+1) for all c


        # initial dp array
        dp = [float('inf')] * (amount + 1) 
        dp[0] = 0

        for c in coins:
            # Traverse amounts in forward order so that
            # the current coin can be used multiple times.
            for m in range(c, amount+1):
                # Option 1: Do not use the current coin.
                # Option 2: Use one more current coin.
                dp[m] = min(dp[m], dp[m-c]+1)  
        
        ans = dp[amount]

        return ans if ans < float('inf') else -1                    
        
# @lc code=end

