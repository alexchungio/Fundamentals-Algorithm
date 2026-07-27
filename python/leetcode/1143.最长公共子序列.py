#
# @lc app=leetcode.cn id=1143 lang=python3
#
# [1143] 最长公共子序列
#

# @lc code=start
class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:

        # dp[i][j] represents the length of the longest common subsequence
        # between the first i characters of text1 and the first j characters of text2.

        # initial dp table
        dp = [[0 for _ in range(len(text2)+1)] for _ in range(len(text1)+1)]

        ans = 0
        for i in range(1, len(text1) + 1):
            for j in range(1, len(text2) + 1):
                
                # Compare current characters.
                # text1[i-1] and text2[j-1] are the actual indices.
                
                # If characters are equal,
                # extend the previous LCS by 1.
                if text1[i-1] == text2[j-1]:  
                    dp[i][j] = dp[i-1][j-1] + 1
                else: 

                    # If characters are different,
                    # choose the better result.
                    dp[i][j] = max(dp[i-1][j], dp[i][j-1])

                # update result
                ans = max(ans, dp[i][j])

        return ans
        
# @lc code=end

