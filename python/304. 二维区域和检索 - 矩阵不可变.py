"""
304. 二维区域和检索 - 矩阵不可变
给定一个二维矩阵，计算其子矩形范围内元素的总和，
该子矩阵的左上角为 (row1, col1) ，右下角为 (row2, col2) 。

3, 0, 1, 4 , 2
5, 6, 3, 2 , 1
1,[2, 0, 1], 5
4,[1, 0, 1], 7
1,[0, 3, 0], 5
上图子矩阵左上角 (row1, col1) = (2, 1) ，右下角(row2, col2) = (4, 3)，
该子矩形内元素的总和为 8。


示例：

给定 matrix = [
  [3, 0, 1, 4, 2],
  [5, 6, 3, 2, 1],
  [1, 2, 0, 1, 5],
  [4, 1, 0, 1, 7],
  [1, 0, 3, 0, 5]
]

sumRegion(2, 1, 4, 3) -> 8
sumRegion(1, 1, 2, 2) -> 11
sumRegion(1, 2, 2, 4) -> 12

提示：
你可以假设矩阵不可变。
会多次调用 sumRegion 方法。
你可以假设 row1 ≤ row2 且 col1 ≤ col2 。

date: 2021年3月2日
"""

from typing import List


class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        # todo 二维前缀和
        row, col = len(matrix), len(matrix[0]) if matrix else 0
        # preSum 矩阵比原矩阵多一行一列 保证公式通用
        self.preSum = [[0]*(col + 1) for _ in range(row + 1)]

        _sum = self.preSum
        for i in range(row):
            for j in range(col):
                _sum[i+1][j+1] = _sum[i][j+1] + \
                    _sum[i+1][j] - _sum[i][j] + matrix[i][j]

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        _sum = self.preSum
        return _sum[row2+1][col2+1] - _sum[row1][col2+1] - _sum[row2+1][col1] + _sum[row1][col1]


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)
matrix = [
    [3, 0, 1, 4, 2],
    [5, 6, 3, 2, 1],
    [1, 2, 0, 1, 5],
    [4, 1, 0, 1, 7],
    [1, 0, 3, 0, 5]
]
NumMatrix = NumMatrix(matrix)
sum1 = NumMatrix.sumRegion(0, 0, 2, 2)
print(sum1)
