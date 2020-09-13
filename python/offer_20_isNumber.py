"""
剑指 Offer 20. 表示数值的字符串

请实现一个函数用来判断字符串是否表示数值（包括整数和小数）。
例如，字符串"+100"、"5e2"、"-123"、"3.1416"、"-1E-16"、"0123"都表示数值，
但"12e"、"1a3.14"、"1.2.3"、"+-5"及"12e+5.4"都不是。

date: 9-2-2020

知识点：确定有限状态自动机
"""

class Solution:
    def isNumber(self, s: str) -> bool:
        """
        :type s: str
        :rtype: bool
        """
        # 定义状态转移表
        states = [
            {' ':0, 'sign':1, 'digit':2, '.':4}, # 0. start with 'blank'
            {'digit':2, '.':4}, # 1. 'sign' before 'e'
            {'digit':2, '.':3, 'e':5, ' ':8}, # 2. 'digit' before 'dot'
            {'digit':3, 'e':5, ' ':8}, # 3. 'digit' after 'dot'
            {'digit':3}, # 4. 'dot' and 'digit' after 'dot' (‘blank’ before 'dot')
            {'sign':6, 'digit':7}, # 5. 'e'
            {'digit':7}, # 6. 'sign' after 'e'
            {'digit':7, ' ':8}, # 7. 'digit' after 'e'
            {' ':8}, # 8. end with 'blank'
        ]

        state = 0   # start with state 0
        # 状态转移循环
        for c in s:
            if '0' <= c <= '9':
                target = 'digit'
            elif c in "+-":
                target = 'sign'
            elif c in "eE":
                target = 'e'
            elif c in ". ":
                target = c
            else:
                target = '?'
            if target not in states[state]:
                return False
            state = states[state][target]
        return state in (2, 3, 7, 8)

    def isNumber_cheat(self, s):
        """
        :type s: str
        :rtype: bool
        """
        try:
            float(s)
        except:
            return False
        return  True



s = Solution()
str = "-1E-16"
print(s.isNumber(str))
print(s.isNumber_cheat(str))
