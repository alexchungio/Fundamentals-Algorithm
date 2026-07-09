#
# @lc app=leetcode.cn id=344 lang=python3
#
# [344] 反转字符串
#

# @lc code=start
class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        
        for i in range(len(s)):
            j = len(s) - 1 - i
            
            if i < j:
                s = self.swap(s, i, j)

        return s

    
    def swap(self, s, i, j):
        tmp = s[i]
        s[i] = s[j]
        s[j]  = tmp

        return s          
        
        
# @lc code=end

