"""
46. 全排列
给定一个 没有重复 数字的序列，返回其所有可能的全排列。

示例:

输入: [1,2,3]
输出:
[
  [1,2,3],
  [1,3,2],
  [2,1,3],
  [2,3,1],
  [3,1,2],
  [3,2,1]
]
"""
from typing import List

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        """
        回溯类题一定要考虑的几个方面:
        有效结果：当长度为输入长度的时候停止，并保存当前结果
        回溯条件：每一层都是全部元素遍历：例如答案为[2,1,3]时，第二个元素也是从1开始
        剪枝条件：要用check数组来保存用过的元素，用过的不能再用了，这是回溯里面的一个重要考虑因素

        Args:
            nums (List[int]): [description]

        Returns:
            List[List[int]]: [description]
        """
        def backTrack(sol: List[int], nums: List, check: List[int]):
            if len(sol) == len(nums):
                res.append(sol)
                return
            
            for i in range(len(nums)):
                if check[i] == 1:
                    continue
                check[i] = 1
                backTrack(sol+[nums[i]], nums, check)
                check[i] = 0

        res, check = [], [0]*len(nums)
        backTrack([], nums, check)
        return res