#
# @lc app=leetcode.cn id=139 lang=python3
#
# [139] 单词拆分
#

# @lc code=start
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:

        # DP(complete knapsack)

        # dp[i] represents whether the first i characters of the string s 
        # can be segmented into words from the dictionary.
        
        # initial dp array
        dp = [False] * (len(s) + 1)
        # Empty string is always a valid segmentation.
        dp[0] = True

        for i in range(1, len(s)+1):
            for j in range(0, i):
                # If the prefix s[0:j] can be segmented
                # and the current substring s[j:i] exists in dictionary,
                # then s[0:i] can also be segmented.
                if s[j:i] in wordDict and dp[j]:
                    dp[i] = True
                    # No need to check other split positions
                    break

        return dp[len(s)]
        
# @lc code=end

