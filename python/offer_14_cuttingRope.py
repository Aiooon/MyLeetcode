"""
剑指 Offer 14- I. 剪绳子 I
给你一根长度为 n 的绳子，请把绳子剪成整数长度的 m 段（m、n都是整数，n>1并且m>1），每段绳子的长度记为 k[0],k[1]...k[m-1] 。
请问 k[0]*k[1]*...*k[m-1] 可能的最大乘积是多少？
例如，当绳子的长度是8时，我们把它剪成长度分别为2、3、3的三段，此时得到的最大乘积是18。

示例 1：
输入: 2
输出: 1
解释: 2 = 1 + 1, 1 × 1 = 1

示例 2:
输入: 10
输出: 36
解释: 10 = 3 + 3 + 4, 3 × 3 × 4 = 36

提示：
2 <= n <= 58

date : 11-4-2020
"""



import math


class Solution:
    def cuttingRope(self, n: int) -> int:
        if n < 2:
            return 0
        elif n == 2:
            return 1
        elif n == 3:
            return 2
        store = [0 for i in range(0, n + 1)]
        store[0], store[1], store[2], store[3] = 0, 1, 2, 3
        for i in range(4, n + 1):
            max = 0
            for j in range(1, (i // 2) + 1):
                temp = (store[j] * store[i-j])
                if max < temp:
                    max = temp
                store[i] = max
        return store[n]

    # 贪婪算法
    def _cuttingRope(self, n: int) -> int:
        if n <= 3:
            return n - 1
        a, b = n // 3, n % 3
        if b == 0:
            return int(math.pow(3, a))
        if b == 1:
            return int(math.pow(3, a - 1) * 4)
        return int(math.pow(3, a) * 2)


print(Solution().cuttingRope(10))

print(1 // 2)

