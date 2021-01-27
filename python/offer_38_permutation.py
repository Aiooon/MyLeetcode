"""
剑指 Offer 38. 字符串的排列
输入一个字符串，打印出该字符串中字符的所有排列。
你可以以任意顺序返回这个字符串数组，但里面不能有重复元素。

示例:
输入：s = "abc"
输出：["abc","acb","bac","bca","cab","cba"]

限制：
1 <= s 的长度 <= 8
"""
from typing import List

class Solution:
    def permutation(self, s: str) -> List[str]:
        """
        全排列
        :param s:
        :return:
        """
        chars, res = list(s), []

        def dfs(x):
            if x == len(s) - 1:
                res.append("".join(chars))
                return
            dic = set()
            for i in range(x, len(chars)):
                if chars[i] in dic:
                    continue
                dic.add(chars[i])
                chars[i], chars[x] = chars[x], chars[i]
                dfs(x + 1)
                chars[i], chars[x] = chars[x], chars[i]

        dfs(0)
        return res


if __name__ == '__main__':
    s = "abc"
    print(list(s))
    print(Solution().permutation(s))
