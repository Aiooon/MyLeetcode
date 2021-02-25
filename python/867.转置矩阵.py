#
# @lc app=leetcode.cn id=867 lang=python3
#
# [867] 转置矩阵
#

# @lc code=start
from typing import List

class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        row, col = len(matrix), len(matrix[0])
        trans = [[0] * row for _ in range(col)]
        for i in range(row):
            for j in range(col):
                trans[j][i] = matrix[i][j]
        return trans



# @lc code=end


matrix = [[1,2,3,4],[4,5,6,7],[6,7,8,9]]
print(Solution().transpose(matrix))
