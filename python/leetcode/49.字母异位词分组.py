#
# @lc app=leetcode.cn id=49 lang=python3
#
# [49] 字母异位词分组
#

# @lc code=start
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        res = []
        str_map = {}
        for s in strs:
            # sorted str as key
            key = ''.join(sorted(s))
            if key in str_map:
                str_map[key].append(s)
            else:
                str_map[key] = [s]
        
        for _, value in str_map.items():
            res.append(value)

        return res
            

# @lc code=end

