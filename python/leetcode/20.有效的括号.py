#
# @lc app=leetcode.cn id=20 lang=python3
#
# [20] 有效的括号
#

# @lc code=start
class Solution:
    def isValid(self, s: str) -> bool:
        
        pairs = {
            '(': ')',
            '{': '}',
            '[': ']',
        }

        stack = list()

        for char in s:
            if char in pairs:
                stack.append(char)
            else:
                if len(stack) > 0:
                    left_char = stack.pop()
                    if pairs[left_char] == char:
                        continue
                    else:
                        return False
                else:
                    return False
                
        return True if len(stack) == 0 else False
        
            
        
# @lc code=end

