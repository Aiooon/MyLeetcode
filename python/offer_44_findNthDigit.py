"""
剑指 Offer 44. 数字序列中某一位的数字
数字以0123456789101112131415…的格式序列化到一个字符序列中。
在这个序列中，第5位（从下标0开始计数）是5，第13位是1，第19位是4，等等。
请写一个函数，求任意第n位对应的数字。

示例 1：
输入：n = 3
输出：3

示例 2：
输入：n = 11
输出：0

限制：0 <= n < 2^31
注意：本题与主站 400 题相同：https://leetcode-cn.com/problems/nth-digit/

date: 2-23-2021
"""

class Solution:
    def findNthDigit(self, n: int) -> int:
        digit, start, count = 1, 1, 9   # 位数，起始数字，个数
        # 1 确定所求数位的所在数字的位数
        while n > count:
            n -= count
            digit += 1
            start *= 10
            count = 9 * start * digit
        # 2 确定所求数位所在的数字
        num = start + (n - 1) // digit
        # 3 确定所求数位在 numnum 的哪一数位
        return int(str(num)[(n - 1) % digit])


if __name__ == '__main__':
    print(Solution().findNthDigit(1000000000))
