#
# @lc app=leetcode.cn id=45 lang=python3
#
# [45] 跳跃游戏 II
#

# @lc code=start
class Solution:
    def jump(self, nums: List[int]) -> int:

        if len(nums) == 1:
            return  0

        cur_farthest = 0
        cur_end = 0
        num_step = 0
        
        #  don't need to iterate the last element, because once we reach or pass it, done
        for i in range(len(nums) - 1):  
            
            # update the farthest position we can reach from the current index
            cur_farthest = max(i+nums[i], cur_farthest)

            # reached the boundary of the current jump range, jump to extend range
            if i == cur_end:
                num_step += 1
                cur_end = cur_farthest
            
        return num_step
      
                
        
# @lc code=end

