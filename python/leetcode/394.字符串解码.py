#
# @lc app=leetcode.cn id=394 lang=python3
#
# [394] 字符串解码
#

# @lc code=start
class Solution:
    def decodeString(self, s: str) -> str:
        
        s_stack = []

        for char in s:
            
            # decoder char 
            if char == ']':
                
                # search [ index
                cur_s = ''
                while s_stack[-1] != '[':
                    cur_s = s_stack.pop() + cur_s

                s_stack.pop() # pop [
                
                # search cur_num
                cur_num = '' # pop num isdigit()
                while s_stack and s_stack[-1].isdigit():
                    cur_num = s_stack.pop() + cur_num
                cur_num = int(cur_num)

                # push decoder str
                s_stack.append(cur_num * cur_s)
            else:
                s_stack.append(char)
                
        return ''.join(s_stack)   
        
        
# @lc code=end

