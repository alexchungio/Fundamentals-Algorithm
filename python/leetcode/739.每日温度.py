#
# @lc app=leetcode.cn id=739 lang=python3
#
# [739] 每日温度
#

# @lc code=start
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        
        answer = [0] * len(temperatures)
        t_stack = []
        
        for i in range(len(temperatures)):
            while(len(t_stack) > 0 and temperatures[t_stack[-1]] < temperatures[i]):
                j = t_stack.pop()
                answer[j] = i - j

            t_stack.append(i)

        return answer
                    
            
        
# @lc code=end

