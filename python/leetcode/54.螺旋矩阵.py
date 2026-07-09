#
# @lc app=leetcode.cn id=54 lang=python3
#
# [54] 螺旋矩阵
#

# @lc code=start
class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        m, n = len(matrix), len(matrix[0]) # h, w
        l, t, r, b = 0, 0, n-1, m-1
        res = []
        while(l <= r and t <= b):
            # left to right
            for i in range(l, r+1):
                res.append(matrix[t][i])
            t += 1

            # top to down
            for i in range(t, b+1):
                res.append(matrix[i][r])
            r -= 1
            
            # recheck range
            if (l <= r and t <= b):

                # top to down
                for i in range(r, l-1, -1):
                    res.append(matrix[b][i])
                b -= 1

                # down to top
                for i in range(b, t-1, -1):
                    res.append(matrix[i][l])
                l += 1

        return res

        
# @lc code=end

