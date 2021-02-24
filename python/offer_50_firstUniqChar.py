"""
剑指 Offer 50. 第一个只出现一次的字符
在字符串 s 中找出第一个只出现一次的字符。如果没有，返回一个单空格。 s 只包含小写字母。

示例:
s = "abaccdeff"
返回 "b"

s = "" 
返回 " "

限制：
0 <= s 的长度 <= 50000

date: 2021年2月24日
"""

class Solution:
    def firstUniqChar(self, s: str) -> str:
        dic = {}
        for c in s:
            if c not in dic:
                dic[c] = True
            else:
                dic[c] = False
        # 遍历有序字典
        for k, v in dic.items():
            if v:
                return k
        return ' '


if __name__ == '__main__':
    print(Solution().firstUniqChar('aaccdxcardeff'))
