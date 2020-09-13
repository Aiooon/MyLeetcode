"""
77. 组合
给定两个整数 n 和 k，返回 1 ... n 中所有可能的 k 个数的组合。

示例:
输入: n = 4, k = 2
输出:
[
  [2,4],
  [3,4],
  [2,3],
  [1,2],
  [1,3],
  [1,4],
]

date: 9-8-2020
"""
from typing import List
import itertools


def combine(n: int, k: int) -> List[List[int]]:
    # numbers = [number for number in range(1, n+1)]
    # for i in range(len(numbers)):

    def DFS(n, k, begin, path, res):
        if len(path) == k:
            res.append(path[:])   # 深拷贝
            # res.append(path[])    浅拷贝，错误的方法
            return
        for i in range(begin, n - (k - len(path)) + 2):
            # 剪枝：搜索起点的上界 + 接下来要选择的元素个数 - 1 = n
            #       搜索起点的上界 = n - (k - len(path)) + 1
            path.append(i)
            DFS(n, k, i+1, path, res)
            path.pop()

    res = []
    if k < 0 or n < k:
        return res
    DFS(n, k , 1, [], res)
    return res


def combine_cheat(n: int, k: int) -> List[List[int]]:
    # numbers = [number for number in range(1, n+1)]
    # for i in range(len(numbers)):
    return list(itertools.combinations(range(1, n + 1), k))


print(combine(4, 2))
