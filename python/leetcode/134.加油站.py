#
# @lc app=leetcode.cn id=134 lang=python3
#
# [134] 加油站
#

# @lc code=start
class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:

        cur_sum = 0 
        total_sum = 0
        start = 0

        for i in range(len(gas)):
            # calculate fuel gain/loss when moving from station i to i+1.
            diff = gas[i] - cost[i]
            # fuel balance from the current station
            cur_sum += diff
            # cumulative fuel balance for the entire trip
            total_sum += diff  

            # search valid start station 
            # If cur_sum drops below 0, it means we cannot reach station i+1 
            # search next and reset cur_sum
            if(cur_sum < 0):
                start = i + 1
                cur_sum = 0

        if total_sum < 0:
            return - 1
        
        return start

# @lc code=end

