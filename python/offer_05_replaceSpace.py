"""
剑指 Offer 05. 替换空格
请实现一个函数，把字符串 s 中的每个空格替换成"%20"。

示例 1：
输入：s = "We are happy."
输出："We%20are%20happy."
 
限制：
0 <= s 的长度 <= 10000
"""

from locale import str


class Solution:
    def replaceSpace(self, s: str) -> str:
        """
        在 Python 和 Java 等语言中，字符串都被设计成不可变的类型，
        即无法直接修改字符串的某一位字符，需要新建一个字符串实现。
        :param s:
        :return:
        """
        res = []
        for char in s:
            if char == ' ':
                res.append("%20")
            else:
                res.append(char)
        return "".join(res)
        # res = []
        # for c in s:
        #     if c == ' ':
        #         res.append("%20")
        #     else:
        #         res.append(c)
        # return "".join(res)

        # 抖机灵 1
        # return s.replace(" ","%20")
        # 抖机灵 2
        # return "".join("%20" if c == " " else c for c in s)



s = Solution()
string = 'we are happy.'
print(s.replaceSpace(string))