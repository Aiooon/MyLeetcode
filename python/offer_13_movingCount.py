"""
剑指 Offer 13. 机器人的运动范围
地上有一个m行n列的方格，从坐标 [0,0] 到坐标 [m-1,n-1] 。
一个机器人从坐标 [0, 0] 的格子开始移动，它每次可以向左、右、上、下移动一格（不能移动到方格外），
也不能进入行坐标和列坐标的数位之和大于k的格子。例如，当k为18时，机器人能够进入方格 [35, 37] ，因为3+5+3+7=18。
但它不能进入方格 [35, 38]，因为 3+5+3+8 = 19。请问该机器人能够到达多少个格子？


示例 1：
输入：m = 2, n = 3, k = 1
 0 / 0
 / 0 0
输出：3

示例 2：
输入：m = 3, n = 1, k = 0
0
/
/
输出：1

提示：
1 <= n,m <= 100
0 <= k <= 20

date : 9-30-2020
"""


class Solution:
    def movingCount(self, m: int, n: int, k: int) -> int:
        if k < 0 or m <= 0 or n <=0:
            return 0

        visited = [False for i in range(m * n)]
        count = self.movingCountCore(m, n, 0, 0, k, visited)

        return count

    def movingCountCore(self, rows, cols, row, col, k, visited):
        count = 0
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        if self.check(rows, cols, row, col, k, visited):
            count += 1
            visited[row*cols + col] = True
            for step_row, step_col in directions:
                count += self.movingCountCore(rows, cols, row + step_row, col + step_col, k, visited)

        return count

    def check(self, rows, cols, x, y, k, visited):
        return True if (0 <= x < rows and 0 <= y < cols) and (self.sums(x) + self.sums(y) <= k)\
                and not visited[x*cols + y] else False

    # 计算数位之和
    def sums(self, x: int):
        res = 0
        while x != 0:
            res += x % 10
            x = x // 10

        return res


"""
0 0
0 0
"""

m = 2
n = 3
k = 1
print(Solution().movingCount(m, n, k))
