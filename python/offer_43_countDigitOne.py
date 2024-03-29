"""
剑指 Offer 43. 1～n 整数中 1 出现的次数
输入一个整数 n ，求1～n这n个整数的十进制表示中1出现的次数。
例如，输入12，1～12这些整数中包含1 的数字有1、10、11和12，1一共出现了5次。

示例 1：
输入：n = 12
输出：5

示例 2：
输入：n = 13
输出：6

限制：1 <= n < 2^31
注意：本题与主站 233 题相同：https://leetcode-cn.com/problems/number-of-digit-one/

date : 2-23-2021
"""

class Solution:
    # overtime
    # def count(self, num: str):
    #     count = 0
    #     for c in num:
    #         if c == '1':
    #             count += 1
    #     return count
    # def countDigitOne(self, n: int) -> int:
    #     count = 0
    #     for i in range(n + 1):
    #         count += self.count(str(i))
    #     return count

    # right answer
    def countDigitOne(self, n: int) -> int:
        # init
        res = 0
        low = 0
        cur = n % 10
        high = n // 10
        digit = 1
        # recur
        while high != 0 or cur != 0:
            if cur == 0:
                res += high * digit
            elif cur == 1:
                res += high * digit + low + 1
            else:
                res += (high + 1) * digit
            # update
            low += cur * digit
            cur = high % 10
            high = high // 10
            digit *= 10

        return res


if __name__ == '__main__':
    print(Solution().countDigitOne(824883294))
