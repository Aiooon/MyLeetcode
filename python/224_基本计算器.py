"""
224. 基本计算器
实现一个基本的计算器来计算一个简单的字符串表达式 s 的值。

示例 1：
输入：s = "1 + 1"
输出：2

示例 2：
输入：s = " 2-1 + 2 "
输出：3

示例 3：
输入：s = "(1+(4+5+2)-3)+(6+8)"
输出：23

提示：
1 <= s.length <= 3 * 105
s 由数字、'+'、'-'、'('、')'、和 ' ' 组成
s 表示一个有效的表达式

date: 2021年3月10日
"""


class Solution:
    def calculate(self, s: str) -> int:
        """
        维护一个栈 ops 记录当前括号内的整体符号

        Args:
            s (str): [description]

        Returns:
            int: [description]
        """
        ops, sign, res, l, i = [1], 1, 0, len(s), 0
        while i < l:
            if s[i] == ' ':
                i += 1
            elif s[i] == '+':
                sign = ops[-1]
                i += 1
            elif s[i] == '-':
                sign = -ops[-1]
                i += 1
            elif s[i] == '(':
                ops.append(sign)
                i +=1
            elif s[i] == ')':
                ops.pop()
                i += 1
            else:
                num = 0
                while i < l and '0' <= s[i] <= '9':
                    num = num * 10 + int(s[i])
                    i += 1
                res += sign * num
        return res

s = "-(1 + 2 - (3 + 4))"
print(Solution().calculate(s))
