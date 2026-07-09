#
# @lc app=leetcode.cn id=34 lang=python3
#
# [34] 在排序数组中查找元素的第一个和最后一个位置
#

# @lc code=start
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:

        if len(nums) == 0:
            return [-1, -1]

        left_idx = self.binary_search_left_boundary(nums, target, 0, len(nums) - 1)
        
        # target not exist, return
        if left_idx == len(nums) or nums[left_idx] != target:
            return [-1, -1]
        
        right_idx = self.binary_search_right_boundary(nums, target, left_idx+1, len(nums) - 1)
        # right_idx = self.binary_search_right_boundary(nums, target, 0, len(nums) - 1)
        
        return [left_idx, right_idx]
    

    def binary_search_left_boundary(self, nums, target, left, right):
        
        left -= 1
        right += 1

        while left+1 != right:

            print(left, right)
            
            mid = (left + right) // 2

            if nums[mid] < target:
                left = mid
            else:
                right = mid 
        
        return right
    
    
    def binary_search_right_boundary(self, nums, target, left, right):
        
        left -= 1
        right += 1

        while left+1 != right:

            mid = (left + right) // 2
            
            if nums[mid] <= target:
                left = mid
            else:
                right = mid 
        
        return left       
        
# @lc code=end

