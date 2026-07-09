#
# @lc app=leetcode.cn id=121 lang=python3
#
# [121] 买卖股票的最佳时机
#

# @lc code=start
class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        ans = 0
        low_value = prices[0]  # record low value
        for i in range(len(prices)):
            
            ans = max(prices[i] - low_value, ans)
            low_value = min(prices[i], low_value)

        return ans
       
            
        
# @lc code=end

