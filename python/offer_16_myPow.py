"""
剑指 Offer 16. 数值的整数次方
实现函数double Power(double base, int exponent)，求base的exponent次方。
不得使用库函数，同时不需要考虑大数问题。


示例 1:
输入: 2.00000, 10
输出: 1024.00000

示例 2:
输入: 2.10000, 3
输出: 9.26100

示例 3:
输入: 2.00000, -2
输出: 0.25000

解释: 2-2 = 1/22 = 1/4 = 0.25


说明:
-100.0 < x < 100.0
n 是 32 位有符号整数，其数值范围是 [−2^31, 2^31 − 1] 。


date : 11-30-2020
"""

class Solution:
    def myPow(self, x: float, n: int) -> float:
        if x == 0.:
            return 0
        if n == 0:
            return 1
        if n == 1:
            return x
        if n < 0:
            x = 1 / x
            n = -n
        res = self.myPow(x, n >> 1)
        res *= res
        if n & 1 == 1:
            res *= x
        return res


print(Solution().myPow(2., 10))
print(Solution().myPow(0.00001, 2147483647))
# print(Solution().myPow(2., -2))

