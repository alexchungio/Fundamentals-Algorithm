#
# @lc app=leetcode.cn id=3 lang=python3
#
# [3] 无重复字符的最长子串
#

# @lc code=start
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        ans = 0
        left = 0
        unique_map = {} # store char:last_index

        for right, char in enumerate(s):
            # update left to next index
            if char in unique_map and unique_map[char] >= left:
                left = unique_map[char] + 1

            # update last index of char
            unique_map[char] = right
            
            ans = max(right - left + 1, ans)

        return ans
                
        
# @lc code=end

