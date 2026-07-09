#
# @lc app=leetcode.cn id=131 lang=python
#
# [131] 分割回文串
#

# @lc code=start
class Solution(object):
    def partition(self, s):
        """
        :type s: str
        :rtype: List[List[str]]
        """

        res = []
        path = []

        def backtracking(s, start):
            # nonlocal path
            # no stop condition
            if start == len(s):
                res.append(path[:])
                return
            
            for i in range(start, len(s)):
                
                s_tmp = s[start: i+1]
                
                if s_tmp == s_tmp[::-1]:
                    path.append(s_tmp)
                    backtracking(s, i+1)
                    path.pop()
                
        backtracking(s, 0)

        return res
        
# @lc code=end

