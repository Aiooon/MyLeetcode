"""
剑指 Offer 03. 数组中重复的数字
找出数组中重复的数字。

在一个长度为 n 的数组 nums 里的所有数字都在 0～n-1 的范围内。数组中某些数字是重复的，但不知道有几个数字重复了，
也不知道每个数字重复了几次。请找出数组中任意一个重复的数字。

示例 1：

输入：
    [2, 3, 1, 0, 2, 5, 3]
    输出：2 或 3

限制：
    2 <= n <= 100000

date : 9-17-2020
"""
from typing import List


class Solution:
    def findRepeatNumber(self, nums: List[int]) -> int:
        """

        :param nums:
        :return:
        """
        length = len(nums)
        for i in range(length):
            if nums[i] < 0 or nums[i] > length - 1:
                return -1
            while nums[i] != i:
                if nums[i] == nums[nums[i]]:
                    return nums[i]
                nums[nums[i]], nums[i] = nums[i], nums[nums[i]]

        return -1


    # 原地交换标答
    def findRepeatNumber_ans(self, nums: [int]) -> int:
        if nums is None:
            return -1

        for i in range(len(nums)):
            if nums[i] == i:
                i += 1
                continue
            if nums[i] == nums[nums[i]]:
                return nums[i]
            nums[i], nums[nums[i]] = nums[nums[i]], nums[i]
            return -1



s = Solution()
nums = [1, 2, 3, 4, 2, 3]
nums_ = [1, 2, 3, 0]
nums__ = [2, 3, 1, 0, 2, 5, 3]
print(s.findRepeatNumber(nums))
print(s.findRepeatNumber(nums_))
print(s.findRepeatNumber(nums__))
print(s.findRepeatNumber_ans(nums__))
