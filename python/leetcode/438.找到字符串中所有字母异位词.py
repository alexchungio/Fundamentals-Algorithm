#
# @lc app=leetcode.cn id=438 lang=python3
#
# [438] 找到字符串中所有字母异位词
#

# @lc code=start
class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:

        res = []
        
        if len(s) < len(p):
            return res

        # store count of char
        # a's ascll is 97
        s_count = [0] * 26
        p_count = [0] * 26

        # stat p
        for idx in range(len(p)):
            p_count[ord(p[idx]) - 97] += 1
            s_count[ord(s[idx]) - 97] += 1

        
        if p_count == s_count:
            res.append(0)

        for idx in range(len(p), len(s)):
            s_count[ord(s[idx]) - 97] += 1  # add right count
            s_count[ord(s[idx - len(p)]) - 97] -= 1  # reduce left count

            if s_count == p_count:
                res.append(idx - len(p)+1) 

        return res
                
         
        
# @lc code=end

