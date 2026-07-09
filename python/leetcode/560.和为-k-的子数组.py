#
# @lc app=leetcode.cn id=560 lang=python3
#
# [560] 和为 K 的子数组
#

# @lc code=start
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:

        
        ans = 0
        prefix_count = {}
        
        cur_sum = 0
        for num in nums:
            cur_sum += num

            # check sum of current 
            if cur_sum == k:
                ans += 1

            # check sum from history to current 
            if cur_sum - k in prefix_count:
                ans += prefix_count[cur_sum - k]

            # update prefix_count
            if cur_sum in prefix_count:
               prefix_count[cur_sum] += 1
            else:
                prefix_count[cur_sum] = 1
        
        return ans            
            
        
# @lc code=end

