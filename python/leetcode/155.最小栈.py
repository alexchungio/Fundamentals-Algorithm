#
# @lc app=leetcode.cn id=155 lang=python3
#
# [155] 最小栈
#

# @lc code=start
class MinStack:

    def __init__(self):
        self.stack = list()
        self.min_stack = [float('inf')]

    def push(self, value: int) -> None:
        self.stack.append(value)
        self.min_stack.append(min(self.min_stack[-1], value))
        


    def pop(self) -> None:
        
        self.min_stack.pop()

        return self.stack.pop()
        

    def top(self) -> int:

        return self.stack[-1]
        

    def getMin(self) -> int:

        return self.min_stack[-1]
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(value)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
# @lc code=end

