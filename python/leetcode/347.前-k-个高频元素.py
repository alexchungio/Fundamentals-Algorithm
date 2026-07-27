#
# @lc app=leetcode.cn id=347 lang=python3
#
# [347] 前 K 个高频元素
#

# @lc code=start
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # Use a min-heap with at top-k frequent elements.
       
        freq = {}
        for num in nums:
            if num in freq:
                freq[num] += 1
            else:
                freq[num] = 1

         # store a min-heap of size k.
        # Each element in the heap is (frequency, number).
        heap = []

        for num, count in freq.items():
            # Push the current (frequency, number) pair.
            heapq.heappush(heap, (count, num))

            if len(heap) > k:
                heapq.heappop(heap)

        # Extract the numbers from the heap.
        # Reverse the result so that elements are ordered
        # from higher to lower frequency.
        return [n for _, n in heap][::-1]
        
# @lc code=end

