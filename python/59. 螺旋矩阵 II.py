

from typing import List

class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        left, right = 0, n - 1   # 列数的遍历范围  左 <-> 右
        top, bot = 0, n - 1           # 行数的遍历范围  上 <-> 下
        res = [[0 for _ in range(n)] for _ in range(n)]
        num, end = 1, n * n
        while num <= end:
            for i in range(left, right + 1):    # 从左至右
                res[top][i] = num
                num += 1
            top += 1
            
            for i in range(top, bot + 1):   # 从上至下
                res[i][right] = num
                num += 1
            right -= 1
            
            for i in range(right, left - 1, -1):     # 从右至左
                res[bot][i] = num
                num += 1
            bot -= 1

            for i in range(bot, top - 1, -1):       # 从下至上
                res[i][left] = num
                num += 1
            left += 1
            
        return res


print(Solution().generateMatrix(3))