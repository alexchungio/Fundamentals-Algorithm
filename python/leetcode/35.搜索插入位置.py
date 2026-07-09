#
# @lc app=leetcode.cn id=35 lang=python
#
# [35] 搜索插入位置
#

# @lc code=start
class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """

        n = len(nums)    
        left = 0
        right = n-1

        # left ->  vallue < target, right -> value >= target
        while left <= right:
            mid = (left + right) // 2

            if nums[mid] < target:
                left = mid + 1
            elif nums[mid] > target:
                right = mid - 1  
            else:
                return mid
                
        ans = left  # return right boundary

        return ans   
    

    def searchInsert_open(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """

        n = len(nums)    
        left = -1
        right = n

        # left ->  vallue < target, right -> value >= target
        while left + 1 != right:
            mid = (left + right) // 2

            if nums[mid] < target:
                left = mid
            else:
                right = mid  
                
        ans = right  # return right boundary

        return ans 
        
# @lc code=end

