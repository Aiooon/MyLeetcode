"""
131. 分割回文串
给定一个字符串 s，将 s 分割成一些子串，使每个子串都是回文串。

返回 s 所有可能的分割方案。

示例:

输入: "aab"
输出:
[
["aa","b"],
["a","a","b"]
]

date: 2021年3月7日
"""
from typing import List
import copy

class Solution:
    def partition(self, s: str) -> List[List[str]]:
        # todo 回溯 + 动态规划
        """
        用动态规划记录所有字串是否是回文
        回溯递归

        回溯问题抓住三个要点：
        1.选择，当前你有什么选择，一个选择代表一个分支，基于一种选择，又会展开出一些选择
        2.约束条件，利用它去做剪枝，减少不必要的搜索，让你的搜索树“瘦身”
        3.目标，明确了何时将部分解加入解集，结束当前的递归
        
        模板 choose -- explore -- unchoose：
        1.用 for 循环枚举出当前的选择
        2.作出一个选择，基于这个选择，继续递归
        3.递归结束了，撤销这个选择，进入下一轮迭代

        Args:
            s (str): [description]

        Returns:
            List[List[str]]: [description]

        beats：10%

        """
        l, res = len(s), []
        # dp = [[0] * l] * l      # 错误的数组创建方法：浅拷贝，会导致同时更新
        dp = [[0 for _ in range(l)] for _ in range(l)]
        for i in range(l):
            for j in range(i + 1):
                if i == j:
                    dp[j][i] = 1
                elif i - j == 1 and s[i] == s[j]:
                    dp[j][i] = 1
                elif i - j > 1 and s[i] == s[j] and dp[j+1][i-1]:
                    dp[j][i] = 1
                else:
                    dp[j][i] = 0

        def dfs(sol, start):
            if start == l:
                # res.append(sol)   # 错误的方法 浅拷贝
                res.append(copy.deepcopy(sol)) # 正确方法 深拷贝
                return
            for i in range(start, l):
                if dp[start][i]:
                    sol.append(s[start : i+1])
                    dfs(sol, i + 1)
                    sol.pop()
        dfs([], 0)
        return res
    
    def better_partition(self, s: str) -> List[List[str]]:
        """
        回溯模板：
        res = []
        path = []

        def backtrack(未探索区域, res, path):
            if 未探索区域满足结束条件:
                res.add(path) # 深度拷贝
                return
            for 选择 in 未探索区域当前可能的选择:
                if 当前选择符合要求:
                    path.add(当前选择)
                    backtrack(新的未探索区域, res, path)
                    path.pop()

        Args:
            s (str): [description]

        Returns:
            List[List[str]]: [description]
        
        beats:  用时63.31% 内存86.2%

        """
        def backtrack(remain_s, path, res):
            if not remain_s:
                res.append(path)
                return
            for i in range(1, len(remain_s) + 1):
                if self.isPalindrome(remain_s[:i]):
                    backtrack(remain_s[i:], path + [remain_s[:i]], res)

        self.isPalindrome = lambda s : s == s[::-1]    # 判断回文
        res = []
        backtrack(s, [], res)
        return res



s = 'aab'
print(Solution().partition(s))
print(Solution().better_partition(s))
