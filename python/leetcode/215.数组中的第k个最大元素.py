#
# @lc app=leetcode.cn id=215 lang=python3
#
# [215] 数组中的第K个最大元素
#

# @lc code=start
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # Use a min-heap with at most k elements.
    
        # The heap always stores the k largest elements seen so far.
        heap = []
        for num in nums:
            # Push the current number into the heap.
            heapq.heappush(heap, num)

            # If the heap size exceeds k,
            # remove the smallest element.
            # This keeps only the k largest elements.
            if len(heap) > k:
                 heapq.heappop(heap)

        # The root of the min-heap is the kth largest element.
        return heap[0]
                  
# @lc code=end

