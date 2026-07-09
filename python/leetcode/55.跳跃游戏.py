#
# @lc app=leetcode.cn id=55 lang=python3
#
# [55] 跳跃游戏
#

# @lc code=start
class Solution:
    def canJump(self, nums: List[int]) -> bool:

        farthest = 0
        idx = 0
        
        while idx < len(nums):
            
            # if the current index cannot be reached, stop
            if idx > farthest:
                
                return False
            
            # search farthest boundary from the current reachable position
            farthest = max(idx + nums[idx], farthest)

            # early stop, if the farthest boundary already covers or passes the last index
            if farthest >= len(nums) - 1:
                return True
            
            # update idx
            idx += 1
    
        return True
             
        
# @lc code=end

