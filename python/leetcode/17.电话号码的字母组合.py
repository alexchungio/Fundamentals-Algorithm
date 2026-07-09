#
# @lc app=leetcode.cn id=17 lang=python3
#
# [17] 电话号码的字母组合
#

# @lc code=start

tables = ['', '', 'abc', 'def', 'ghi', 'jkl', 'mno', 'pqrs', 'tuv', 'wxyz']

class Solution:

    def letterCombinations(self, digits: str) -> List[str]:

        res = []
        path = []
        def backtracking(digits, level):
            # stop condition
            nonlocal path
            if len(path) == len(digits):
                res.append(''.join(path[:]))
                return

            s = tables[int(digits[level])] 
            print(s)
            for i in range(0, len(s)):
                print(i)
                path.append(s[i])
                # dfs
                backtracking(digits, level+1)
                path.pop()
                
        backtracking(digits, 0)

        return res
        
# @lc code=end

