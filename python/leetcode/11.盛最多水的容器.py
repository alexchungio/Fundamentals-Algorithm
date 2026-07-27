#
# @lc app=leetcode.cn id=11 lang=python3
#
# [11] 盛最多水的容器
#

# @lc code=start
class Solution:
    def maxArea(self, height: List[int]) -> int:
        
        # Store the maximum area found so far
        max_area = 0

        # Initialize two pointers at both ends of the array
        left = 0
        right = len(height) - 1
        
        # Move pointers toward each other until they meet to search max area
        while left < right:
            
            # Calculate current container area
            # Height is limited by the shorter boundary
            # Width is the distance between two pointers
            area = min(height[left], height[right]) * (right-left)

            # Update maximum area
            max_area = max(area, max_area)
            
            # move point at small boundary to search max area , 
            # otherwise the max area will not exceed current max area
            if height[left] <= height[right]:
                left += 1
            else:
                right -= 1

        return max_area
                
        
# @lc code=end

