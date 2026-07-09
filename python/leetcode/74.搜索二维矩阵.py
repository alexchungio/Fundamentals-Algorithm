#
# @lc app=leetcode.cn id=74 lang=python3
#
# [74] 搜索二维矩阵
#

# @lc code=start
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        m = len(matrix)
        n = len(matrix[0])


        # search row
        row_idx = self.binary_search_matrix(matrix, target, left=0, right=m-1, column=0)

        if row_idx == -1 or row_idx == m:
            return False
        

        # search column
        col_idx = self.binary_search_matrix(matrix, target, left=0, right=n-1, row=row_idx)

        if col_idx == -1 or col_idx == n:
             return False
        
        if matrix[row_idx][col_idx] == target:
            return True
        else:
            return False
        


    def binary_search_matrix(self, matrix, target, left, right, column=None, row=None):

        left -= 1
        right += 1

        while left+1 != right:
            
            # search by row
            if column is not None:
                mid = (left + right) // 2
                if matrix[mid][column] <= target:
                    left = mid
                else:
                    right = mid
            # search by column
            else:
                mid = (left + right) // 2
                if matrix[row][mid] <= target:
                    left = mid
                else:
                    right = mid

        return left
                    
# @lc code=end

