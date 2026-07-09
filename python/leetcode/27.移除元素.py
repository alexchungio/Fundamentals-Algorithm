#
# @lc app=leetcode.cn id=27 lang=python3
#
# [27] 移除元素
#

# @lc code=start
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        
        slow_ptr = 0  # record the idx(number) of do not equal val
        for fast_ptr in range(0, len(nums)):
            if (nums[fast_ptr] != val):
                nums[slow_ptr] = nums[fast_ptr]
                slow_ptr += 1

        return slow_ptr


        
# @lc code=end

