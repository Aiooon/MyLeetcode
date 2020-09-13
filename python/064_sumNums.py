#-*-coding:utf-8-*-

# 手动设置递归调用深度
import sys
sys.setrecursionlimit(10000000)
"""
Python中默认的最大递归深度是989，当尝试递归第990时便出现递归深度超限的错误：
RecursionError: maximum recursion depth exceeded in comparison
"""

class Solution:
    def __init__(self):
        self.res = 0
    def sumNums(self, n: int) -> int:
        """
        求 1+2+...+n ，要求不能使用乘除法、for、while、if、else、switch、case等关键字及条件判断语句（A?B:C）。
        示例 1：
            输入: n = 3
            输出: 6
        示例 2：
            输入: n = 9
            输出: 45
        限制：
            1 <= n <= 10000
        :param n: margin
        :return: sum of 1+2+...+n
        """
        n > 1 and self.sumNums(n-1)
        self.res += n
        return self.res

s = Solution()
n = 1000
print(s.sumNums(n))

# print(2 and 3)
