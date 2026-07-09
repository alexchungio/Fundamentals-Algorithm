#
# @lc app=leetcode.cn id=455 lang=python3
#
# [455] 分发饼干
#

# @lc code=start
class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        
        g = sorted(g)
        s = sorted(s)

        ans = 0
        g_idx = 0
        s_idx = 0
        
        while g_idx < len(g) and s_idx < len(s):
        
            if s[s_idx] >= g[g_idx]:
                ans += 1
                g_idx += 1
                s_idx += 1 
            else:
                s_idx += 1

        return ans
                            
        
# @lc code=end

