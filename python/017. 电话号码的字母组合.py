"""
17. 电话号码的字母组合
给定一个仅包含数字 2-9 的字符串，返回所有它能表示的字母组合。答案可以按 任意顺序 返回。
给出数字到字母的映射如下（与电话按键相同）。注意 1 不对应任何字母。

示例 1：

输入：digits = "23"
输出：["ad","ae","af","bd","be","bf","cd","ce","cf"]
示例 2：

输入：digits = ""
输出：[]
示例 3：

输入：digits = "2"
输出：["a","b","c"]

date: 2021年3月26日
"""
from typing import List

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []

        idx2chr = [ [], [], ['a', 'b', 'c'], 
                            ['d', 'e', 'f'],
                            ['g', 'h', 'i'], 
                            ['j', 'k', 'l'], 
                            ['m', 'n', 'o'], 
                            ['p', 'q', 'r', 's'], 
                            ['t', 'u', 'v'], 
                            ['w', 'x', 'y', 'z']]
        res = []

        def backtrack(sol, res, digits_idx):
            if len(sol) == len(digits):
                res.append(sol)
                return
            chars = idx2chr[int(digits[digits_idx])]
            for c in chars:
                sol += c
                backtrack(sol, res, digits_idx + 1)
                sol = sol[:-1]

        backtrack("", res, 0)
        return res

digits = "23"
print(Solution().letterCombinations(digits))