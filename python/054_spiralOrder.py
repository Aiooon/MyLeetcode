from typing import List
import numpy as np

class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        """
        输入一个矩阵，按照从外向里以顺时针的顺序依次打印出每一个数字。
        示例 1：
            输入：matrix = [[1,2,3],[4,5,6],[7,8,9]]
            输出：[1,2,3,6,9,8,7,4,5]
        示例 2：
            输入：matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
            输出：[1,2,3,4,8,12,11,10,9,5,6,7]
        限制：
            0 <= matrix.length <= 100
            0 <= matrix[i].length <= 100
        :param matrix:
        :return:
        """
        if not matrix:
            return []
        left, right, top, bottom, ans = 0, len(matrix[0]) - 1, 0, len(matrix) - 1, []

        while True:
            for i in range(left, right + 1):  # 从左至右
                ans.append(matrix[top][i])
            top += 1
            if top > bottom:
                break

            for i in range(top, bottom + 1):    # 从上至下
                ans.append(matrix[i][right])
            right -= 1
            if left > right:
                break

            for i in range(right, left - 1, -1):    # 从右至左
                ans.append(matrix[bottom][i])
            bottom -= 1
            if top > bottom:
                break

            for i in range(bottom, top - 1, -1):   # 从下至上
                ans.append(matrix[i][left])
            left += 1
            if left > right:
                break

        return ans




s = Solution()
matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
# 1  2  3  4
# 5  6  7  8
# 9 10 11 12
# print(s.spiralOrder(matrix))
zip1 = zip(matrix)
zip2 = list(zip(*matrix))[::-1]

print(list(zip1))
print(list(zip2))
