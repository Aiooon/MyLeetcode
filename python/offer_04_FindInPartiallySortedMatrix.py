"""
剑指 Offer 04. 二维数组中的查找  //240. 搜索二维矩阵 II

在一个 n * m 的二维数组中，每一行都按照从左到右递增的顺序排序，每一列都按照从上到下递增的顺序排序。
请完成一个函数，输入这样的一个二维数组和一个整数，判断数组中是否含有该整数。

示例:
现有矩阵 matrix 如下：
[
  [1,   4,  7, 11, 15],
  [2,   5,  8, 12, 19],
  [3,   6,  9, 16, 22],
  [10, 13, 14, 17, 24],
  [18, 21, 23, 26, 30]
]
给定 target = 5，返回 true。
给定 target = 20，返回 false。
 
限制：
0 <= n <= 1000
0 <= m <= 1000
"""

from typing import List

class Solution:
    def findNumberIn2DArray(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix:
            return False
        rows, cols = len(matrix), len(matrix[0])  # 当matrix为空时，访问matrix不会报错，但访问matrix[0]会报错
        if rows < 0 or rows > 1000:
            return False
        if cols < 0 or cols > 1000:
            return False

        # print(rows, cols)
        row, col = 0, cols - 1
        while row < rows and col >= 0:
            # 选择右上角的数作为标志数
            if matrix[row][col] == target:
                return True
            elif matrix[row][col] > target:
                col -= 1
            else:
                row += 1
        return False


s = Solution()
# matrix = [
#   [1,   4,  7, 11, 15],
#   [2,   5,  8, 12, 19],
#   [3,   6,  9, 16, 22],
#   [10, 13, 14, 17, 24],
#   [18, 21, 23, 26, 30]]
# target = 100
matrix= []
target = 0
# print(len(matrix), len(matrix[0]))
print(s.findNumberIn2DArray(matrix, target))


