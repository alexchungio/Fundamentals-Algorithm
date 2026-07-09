#
# @lc app=leetcode.cn id=56 lang=python3
#
# [56] 合并区间
#

# @lc code=start
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:

        if len(intervals) == 0:
            return []
        
        # sort the intervals by their start
        # intervals = sorted(intervals, key=lambda x: x[0])
        intervals.sort(key=lambda x: x[0])

        merged = []
        
        for l, r in intervals:
            
            #  merged is empty or the current interval does NOT overlap with the last merged interval
            if len(merged) == 0 or merged[-1][1] < l:
                merged.append([l, r])
            else:
                # update merged, merge the current interval into the last merged interval
                merged[-1][1] = max(merged[-1][1], r)
      
        return merged    
     

# @lc code=end

