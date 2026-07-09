#
# @lc app=leetcode.cn id=763 lang=python3
#
# [763] 划分字母区间
#

# @lc code=start
class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        
        # stat last index for each char
        last = [0] * 26
        for i, char in enumerate(s):
            last[ord(char)-ord('a')] = i

        res = []
        left = 0  # start index of the current partition
        right = 0  # farthest end index of the current partition

        for i, char in enumerate(s):
            
            # extend right boundary of current current partition
            right = max(right, last[ord(char)-ord('a')])

            # reached the end of the current partition, find the boudanry of current partition
            if i == right:
                res.append(right - left + 1)
                left = i+1

        return res
    

# @lc code=end

