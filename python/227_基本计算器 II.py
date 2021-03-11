"""
227. 基本计算器 II
给你一个字符串表达式 s ，请你实现一个基本计算器来计算并返回它的值。
整数除法仅保留整数部分。

示例 1：
输入：s = "3+2*2"
输出：7

示例 2：
输入：s = " 3/2 "
输出：1

示例 3：
输入：s = " 3+5 / 2 "
输出：5

提示：
1 <= s.length <= 3 * 105
s 由整数和算符 ('+', '-', '*', '/') 组成，中间由一些空格隔开
s 表示一个 有效表达式
表达式中的所有整数都是非负整数，且在范围 [0, 2^31 - 1] 内
题目数据保证答案是一个 32-bit 整数

date: 2021年3月11日
"""

class Solution:
    def calculate(self, s: str) -> int:
        """
        思路：先乘除 再加减
        用一个栈保存数字，一个变量 op 保存运算符
        遇到数字时：
            先计算连续数字
            若 op 为 * 或 /，则将栈顶数字出栈，进行乘/除操作后入栈
            若 op 为 + 或 -，则将数字入栈（op 为 - 时乘以 -1 后入栈）
        最后计算栈内所有数据的和

        Args:
            s (str): [description]

        Returns:
            int: [description]
        """
        if not s:
            return 0
        numStack = []
        i, op = 0, ''
        while i < len(s):
            if s[i] == ' ':
                i += 1
            elif s[i] in ['+', '-', '*', '/']:
                op = s[i]
                i += 1
            elif '0' <= s[i] <= '9':
                num = 0
                while i < len(s) and '0' <= s[i] <= '9':
                    num = num * 10 + int(s[i])
                    i += 1
                if op == '+' or op == '':
                    numStack.append(num)
                elif op == '-':
                    numStack.append(-num)
                elif op == '*':
                    numStack.append(numStack.pop() * num)
                elif op == '/':
                    numStack.append(int(numStack.pop() / num))
                
        return sum(numStack)


s = "14-3/2"
print(Solution().calculate(s))
