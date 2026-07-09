#
# @lc app=leetcode.cn id=238 lang=python3
#
# [238] 除了自身以外数组的乘积
#

# @lc code=start
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        ans = [1] * len(nums) # ans as prefix to save memory
        suffix = [1] * len(nums)

        # calcualte preffix
        for idx in range(len(nums) - 1):
            ans[idx+1] = ans[idx] * nums[idx] 

        # calcualte suffix
        for idx in range(len(nums) - 1, 0, -1):
            suffix[idx-1] = suffix[idx] * nums[idx]

        # multi prefix and suffix
        for idx in range(len(nums)):
            ans[idx] *= suffix[idx]

        return ans
            
            
        
# @lc code=end

