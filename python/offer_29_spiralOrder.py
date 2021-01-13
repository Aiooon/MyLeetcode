"""
剑指 Offer 29. 顺时针打印矩阵
输入一个矩阵，按照从外向里以顺时针的顺序依次打印出每一个数字。

示例 1：
输入：matrix = [[1,2,3],
               [4,5,6],
               [7,8,9]]
输出：[1,2,3,6,9,8,7,4,5]

示例 2：
输入：matrix = [[1, 2, 3, 4],
               [5, 6, 7, 8],
               [9,10,11,12]]
输出：[1,2,3,4,8,12,11,10,9,5,6,7]

限制：
0 <= matrix.length <= 100
0 <= matrix[i].length <= 100

注意：本题与主站 54 题相同：https://leetcode-cn.com/problems/spiral-matrix/

date : 1-13-2020
"""
from typing import List


class Solution:
    # Mine fool answer
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        if not matrix:
            return []

        row, col, row_low, col_low = len(matrix), len(matrix[0]), 0, 0
        count = row * col
        row_idx, col_idx = 0, 0
        res = []
        direction = 'R'

        # 转向函数
        def turn(direction: str) -> str:
            if direction == 'R':
                return 'D'  # 向右转为向下
            elif direction == 'D':
                return 'L'  # 向下转为向左
            elif direction == 'L':
                return 'U'  # 向左转为向上
            elif direction == 'U':
                return 'R'  # 向上转为向右

        while len(res) < count:
            """
            1. 遍历行 从左至右 行总数-1
            2. 转向下
            3. 遍历列 从上至下 列总数-1
            4. 转向左
            5. 遍历行 从右至坐 行总数-1
            6. 转向上
            7. 遍历列 从下至上 列总数-1
            8. 转向右 回到第 1 步
            """
            if direction == 'R':  # 从左至右遍历行
                while col_idx < col:
                    res.append(matrix[row_idx][col_idx])
                    col_idx += 1
                col_idx -= 1
                row_idx += 1
                row_low += 1
                direction = turn(direction)
                continue
            if direction == 'D':  # 从上至下遍历列
                while row_idx < row:
                    res.append(matrix[row_idx][col_idx])
                    row_idx += 1
                row_idx -= 1
                col_idx -= 1
                col -= 1
                direction = turn(direction)
                continue
            if direction == 'L':  # 从右至左遍历行
                while col_idx >= col_low:  # bug
                    res.append(matrix[row_idx][col_idx])
                    col_idx -= 1
                col_idx += 1
                row_idx -= 1
                row -= 1
                direction = turn(direction)
                continue
            if direction == 'U':  # 从下至上遍历列
                while row_idx >= row_low:
                    res.append(matrix[row_idx][col_idx])
                    row_idx -= 1
                row_idx += 1
                col_idx += 1
                col_low += 1
                direction = turn(direction)
                continue
        return res

    # better answer
    def _spiralOrder(self, matrix: List[List[int]]) -> List[int]:
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


if __name__ == '__main__':
    matrix = [[1, 2, 3, 4],
              [5, 6, 7, 8],
              [9, 10, 11, 12]]
    print(Solution().spiralOrder(matrix))
