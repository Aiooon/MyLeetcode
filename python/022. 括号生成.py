"""
22. 括号生成
数字 n 代表生成括号的对数，请你设计一个函数，用于能够生成所有可能的并且 有效的 括号组合。

示例 1：
输入：n = 3
输出：["((()))","(()())","(())()","()(())","()()()"]

示例 2：
输入：n = 1
输出：["()"]

提示：

1 <= n <= 8

date: 2021年3月26日
"""
from typing import List

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        
        def dfs(sol, left, right):
            if left == right == 0:
                res.append(sol)
                return 
            if left > right:
                return
            if left > 0:
                dfs(sol + '(', left - 1, right)
            if right > 0:
                dfs(sol + ')', left, right - 1)

        dfs('', n, n)
        return res

print(Solution().generateParenthesis(2))