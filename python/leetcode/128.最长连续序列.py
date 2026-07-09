#
# @lc app=leetcode.cn id=128 lang=python3
#
# [128] 最长连续序列
#

# @lc code=start
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums_set = set(nums)
        longest_num = 0
        
        for num in nums_set:
            if num - 1 not in nums_set:
                curr_num = num
                curr_longest_num = 1
                # only the number is first of the sequence
                while curr_num+1 in nums_set:
                    curr_num = curr_num + 1
                    curr_longest_num += 1
                
                longest_num = max(longest_num, curr_longest_num)

        return longest_num        
                
        
# @lc code=end

