#
# @lc app=leetcode.cn id=15 lang=python3
#
# [15] 三数之和
#

# @lc code=start
class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        
        ans = []
        nums = sorted(nums)

        # a + b + c = 0
        # iteration a
        for i in range(len(nums)):  
            
            # prunning
            if nums[i] > 0:
                return ans
            
            # filter duplicate by a
            if (i > 0 and nums[i] == nums[i-1]):
                continue
            
            # search b, c with two sum
            left = i+1
            right = len(nums) - 1
            while left < right:
                if nums[i] + nums[left] + nums[right] < 0:
                    left += 1
                elif nums[i] + nums[left] + nums[right] > 0:
                    right -= 1
                else:
                    ans.append([nums[i], nums[left], nums[right]])

                    # filter duplicate by b and c
                    while left < right and nums[left+1] == nums[left]:
                        left += 1

                    while left < right and nums[right-1] == nums[left]:
                        right -= 1

                    left += 1
                    right -= 1

        return ans

    
        
# @lc code=end

