"""
54. 螺旋矩阵
给你一个 m 行 n 列的矩阵 matrix，请按照顺时针螺旋顺序，返回矩阵中的所有元素。

示例 1：
输入：matrix = [[1,2,3],
                [4,5,6],
                [7,8,9]]
输出：[1,2,3,6,9,8,7,4,5]

示例 2：
输入：matrix = [[1,2,3,4],
                [5,6,7,8],
                [9,10,11,12]]
输出：[1,2,3,4,8,12,11,10,9,5,6,7]

提示：
m == matrix.length
n == matrix[i].length
1 <= m, n <= 10
-100 <= matrix[i][j] <= 100

date: 2021年3月15日
"""
from typing import List


class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        if not matrix:
            return []
        left, right = 0, len(matrix[0]) - 1   # 列数的遍历范围  左 <-> 右
        top, bot = 0, len(matrix) - 1           # 行数的遍历范围  上 <-> 下
        res = []
        while True:
            for i in range(left, right + 1):  # 从左至右
                res.append(matrix[top][i])
            top += 1
            if top > bot:
                break

            for i in range(top, bot + 1):   # 从上至下
                res.append(matrix[i][right])
            right -= 1
            if left > right:
                break

            for i in range(right, left - 1, -1):     # 从右至左
                res.append(matrix[bot][i])
            bot -= 1
            if bot < top:
                break

            for i in range(bot, top - 1, -1):       # 从下至上
                res.append(matrix[i][left])
            left += 1
            if left > right:
                break

        return res


matrix = [[1, 2, 3],
          [4, 5, 6],
          [7, 8, 9]]
print(Solution().spiralOrder(matrix))
