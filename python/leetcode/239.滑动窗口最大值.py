#
# @lc app=leetcode.cn id=239 lang=python3
#
# [239] 滑动窗口最大值
#

# @lc code=start
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        
        res = []
        #  monotone decreasing‌ queue
        q = collections.deque() # store index

        for i in range(len(nums)):
            
            # make sure the index of left queue in valid range
            if len(q) > 0 and q[0] <= i - k:
                q.popleft()

            # make sure the value in queue sorted in decresing
            while(len(q) > 0 and nums[i] > nums[q[-1]]):
                q.pop()

            # put queue
            q.append(i)

            # filter the value smaller than the minimum interval
            if i >= k - 1:
                res.append(nums[q[0]])

        return res
            
          
# @lc code=end

