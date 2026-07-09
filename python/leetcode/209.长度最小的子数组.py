#
# @lc app=leetcode.cn id=209 lang=python3
#
# [209] 长度最小的子数组
#

# @lc code=start
class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        
        # n = len(nums)
        # length_res = n + 1
        # for slow in range(n):
        #     total = 0
        #     for fast in range(slow, n):
        #         total +=  nums[fast]

        #         if total >= target:
        #             length_res = min(length_res, fast-slow +1)
        #             break

        n = len(nums)
        ans = n + 1
        left = 0
        total = 0

        for right in range(n):
            
            total += nums[right]

            # dynamic fitune left boundary
            while total >= target: 
                ans = min(ans, right - left + 1)
                total -= nums[left]
                left += 1

        
        return 0 if ans == n+1 else ans

                                  
        
# @lc code=end

