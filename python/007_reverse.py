"""
7. 整数反转
给出一个 32 位的有符号整数，你需要将这个整数中每位上的数字进行反转。

示例 1:

输入: 123
输出: 321
 示例 2:

输入: -123
输出: -321
示例 3:

输入: 120
输出: 21
注意:

假设我们的环境只能存储得下 32 位的有符号整数，则其数值范围为 [−2^31,  2^31 − 1]。
请根据这个假设，如果反转后整数溢出那么就返回 0。

date : 9-15-2020
"""
import sys


class Solution:
    def reverse(self, x: int) -> int:
        rev = 0
        if x < 0:
            x = -x
            while x != 0:
                pop = x % 10
                x = int(x / 10)
                rev = rev * 10 + pop
            rev = -rev
        else:
            while x != 0:
                pop = x % 10
                x = int(x / 10)
                rev = rev * 10 + pop
        if rev > 2147483647 or rev < -2147483648:
            return 0
        else:
            return rev

sol = Solution()
x = 123
y = -123
z = 120
a = 1534236469
b = 2147483647
# print(sol.reverse(x))
# print(sol.reverse(y))
# print(sol.reverse(z))

print(sol.reverse(a))
# print(sys.maxsize)
# print(-sys.maxsize - 1)

