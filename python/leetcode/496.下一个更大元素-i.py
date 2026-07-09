#
# @lc app=leetcode.cn id=496 lang=python3
#
# [496] 下一个更大元素 I
#

# @lc code=start
class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        
        # cal value of next larget value and collect by map 
        next_max_map = {num:-1 for num in nums2}
        stack = []
        for idx in range(len(nums2)):
            while(stack and nums2[stack[-1]] < nums2[idx]):
                tmp_idx = stack.pop()
                next_max_map[nums2[tmp_idx]] = nums2[idx]

            stack.append(idx)

        # search res in map
        return [next_max_map[num] for num in nums1]          
            
                

# @lc code=end

