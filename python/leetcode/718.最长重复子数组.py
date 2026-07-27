#
# @lc app=leetcode.cn id=718 lang=python3
#
# [718] 最长重复子数组
#

# @lc code=start
class Solution:
    def findLength(self, nums1: List[int], nums2: List[int]) -> int:
        
        # # dp[i][j] represents the length of the longest common subarray
        # ending at nums1[i-1] and nums2[j-1].

        # initial dp array
        dp = [[0 for _ in range(len(nums2)+1)] for _ in range(len(nums1)+1)]

        ans = 0
        for i in range(1, len(nums1) + 1):
            for j in range(1, len(nums2) + 1):
                # Compare the current elements.
                # nums1[i-1] and nums2[j-1] are the actual indices
                # corresponding to dp[i][j].
                if nums1[i-1] == nums2[j-1]:  
                    # State transition:
                    # If the current elements are equal,
                    # extend the previous common subarray length.
                    dp[i][j] = dp[i-1][j-1] + 1
                ans = max(ans, dp[i][j])

        return ans
              
# @lc code=end

