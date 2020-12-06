"""
118. 杨辉三角
给定一个非负整数 numRows，生成杨辉三角的前 numRows 行。
在杨辉三角中，每个数是它左上方和右上方的数的和。

示例:
输入: 5
输出:
[
[1],
[1,1],
[1,2,1],
[1,3,3,1],
[1,4,6,4,1]
]

date : 12-6-2020
"""
from typing import List


class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        if numRows <= 0:
            return []
        res = [[1]]
        for i in range(1, numRows):
            last_row = res[i - 1]
            new_row = [0] * (i + 1)
            new_row[0], new_row[-1] = 1, 1
            for j in range(1, len(new_row) - 1):
                new_row[j] = last_row[j] + last_row[j - 1]
            res.append(new_row)

        return res


if __name__ == '__main__':
    res = Solution().generate(5)
    l = len(res)
    for item in res:
        print(' '*(l - len(item)), item)

