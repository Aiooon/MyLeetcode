"""
剑指 Offer 46. 把数字翻译成字符串
给定一个数字，我们按照如下规则把它翻译为字符串：
0 翻译成 “a” ，1 翻译成 “b”，……，11 翻译成 “l”，……，25 翻译成 “z”。
一个数字可能有多个翻译。
请编程实现一个函数，用来计算一个数字有多少种不同的翻译方法。
示例 1:
输入: 12258
输出: 5
解释: 12258有5种不同的翻译，分别是"bccfi", "bwfi", "bczi", "mcfi"和"mzi"

提示：0 <= num < 2^31

date: 2021年2月25日
"""


class Solution:
    def translateNum(self, num: int) -> int:
        # todo 动态规划
        s = str(num)
        a = b = 1    # 空数字和数字1的翻译方法都是1种
        for i in range(2, len(s)+1):
            tmp = s[i-2:i]      # tmp 获取数字组合
            c = a + b if '10' <= tmp <= '25' else a
            b = a
            a = c
        return a


print(Solution().translateNum(25))
