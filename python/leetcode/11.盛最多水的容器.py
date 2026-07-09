#
# @lc app=leetcode.cn id=11 lang=python3
#
# [11] 盛最多水的容器
#

# @lc code=start
class Solution:
    def maxArea(self, height: List[int]) -> int:
        
        max_area = 0
        left = 0
        right = len(height) - 1
        
        while left < right:

            area = min(height[left], height[right]) * (right-left)

            max_area = max(area, max_area)
            
            # left point first
            # move point at small boundary to search max area , otherwise the
            # max area will not exceed current max area 
            if height[left] <= height[right]:
                left += 1
            else:
                right -= 1

        return max_area
                
        

        
# @lc code=end

