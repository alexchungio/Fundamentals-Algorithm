#
# @lc app=leetcode.cn id=118 lang=python3
#
# [118] 杨辉三角
#

# @lc code=start
class Solution:
    def generate(self, numRows: int) -> List[List[int]]:

        res = []

        # initial boudanry 
        dp_0 = 1
        res.append([dp_0])

        for i in range(2, numRows+1):

            # dp[n] = [1, *[dp[n-1][i]+dp[n-1][i+1] for i in range(len(dp[n-1])-1)], 1]
            if len(res[-1]) == 1:
                dp_n = [1, *res[-1]]
            else:
                dp_n = [1, *[res[-1][i]+res[-1][i+1] for i in range(len(res[-1])-1)], 1]

            res.append(dp_n)

        return res
# @lc code=end

