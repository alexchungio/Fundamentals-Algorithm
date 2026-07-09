#
# @lc app=leetcode.cn id=33 lang=python3
#
# [33] 搜索旋转排序数组
#

# @lc code=start
class Solution:
    def search(self, nums: List[int], target: int) -> int:

        if len(nums) == 0:
            return - 1
        
        left = 0
        right = len(nums) - 1

        while left <= right:
            
            mid = (left + right) // 2

            if nums[mid] == target:
                return mid

            # checkout order at left or right
            # just consider the order side
            if(nums[left] <= nums[mid]):  # left side is order
                if(target >= nums[left] and target < nums[mid]):
                    right = mid - 1
                else:
                    left = mid + 1
                
            else: # right side is order
                if(target > nums[mid] and target <= nums[right]):
                    left = mid + 1
                else:
                    right = mid - 1

        # print(left)

        return -1

               
# @lc code=end

