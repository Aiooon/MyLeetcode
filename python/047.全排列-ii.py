"""
47. 全排列 II
给定一个可包含重复数字的序列 nums，按任意顺序返回所有不重复的全排列。

示例 1：
输入：nums = [1,1,2]
输出：
[[1,1,2],
 [1,2,1],
 [2,1,1]]

示例 2：
输入：nums = [1,2,3]
输出：[[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]


提示：
1 <= nums.length <= 8
-10 <= nums[i] <= 10

date: 2021年3月6日
"""

from typing import List


class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        # todo 回溯
        """
        考虑重复元素一定要优先排序，将重复的都放在一起，便于找到重复元素和剪枝！！！
        推广至 --> 如果涉及考虑重复元素，或者大小比较的情况，对列表排序是一个不错的选择

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
                if i > 0 and nums[i] == nums[i-1] and check[i-1] == 0:
                    continue
                check[i] = 1
                backTrack(sol+[nums[i]], nums, check)
                check[i] = 0
        nums.sort()
        res, check = [], [0] * len(nums)
        backTrack([], nums, check)
        return res


nums = [1, 1, 2]
print(Solution().permuteUnique(nums))
