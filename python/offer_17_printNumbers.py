"""
剑指 Offer 17. 打印从1到最大的n位数
输入数字 n，按顺序打印出从 1 到最大的 n 位十进制数。比如输入 3，则打印出 1、2、3 一直到最大的 3 位数 999。

示例 1:

输入: n = 1
输出: [1,2,3,4,5,6,7,8,9]


说明：
用返回一个整数列表来代替打印
n 为正整数

相关问题：
大数乘法 大数加法？

date : 12-2-2020
"""
from typing import List


class Solution:
    def printNumbers(self, n: int) -> List[int]:
        if n <= 0:
            return []
        max, res = 9, []
        while n > 1:
            max *= 10
            max += 9
            n -= 1
        for i in range(1, max + 1):
            res.append(i)
        return res

    # 一行代码：
    # return list(range(1, 10 ** n))

    def printNumbers_Pro(self, n: int) -> List[int]:
        """
        正确的思路：考虑大数问题，当 n 很大时上面的方法可能会溢出
        大数的表示应用字符串
        :param n:
        :return:
        """
        if n <= 0:
            return []

        def dfs(x: int):
            if x == n:
                s = ''.join(num[self.startIndex:])
                if s != '0':
                    res.append(int(s))
                if n - self.startIndex == self.numOfNine:
                    self.startIndex -= 1
                return
            for i in range(10):
                num[x] = str(i)
                if i == 9:
                    self.numOfNine += 1
                dfs(x + 1)
            self.numOfNine -= 1

        num = ['0'] * n
        res = []
        self.numOfNine = 0
        self.startIndex = n - 1
        dfs(0)
        return res


# print(Solution().printNumbers_Pro(-1))
# print(Solution().printNumbers_Pro(0))
# print(Solution().printNumbers_Pro(1))
# print(Solution().printNumbers_Pro(2))
print(Solution().printNumbers_Pro(3))
