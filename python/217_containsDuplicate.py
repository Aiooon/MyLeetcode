"""
217. 存在重复元素
给定一个整数数组，判断是否存在重复元素。
如果任意一值在数组中出现至少两次，函数返回 true 。如果数组中每个元素都不相同，则返回 false 。

示例 1:
输入: [1,2,3,1]
输出: true

示例 2:
输入: [1,2,3,4]
输出: false

示例 3:
输入: [1,1,1,3,3,4,3,2,4,2]
输出: true

date : 11-6-2020
"""
from typing import List


class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        box = set()
        length = len(nums)
        if length == 0 or length == 1:
            return False
        for i in range(length):
            if nums[i] not in box:
                box.add(nums[i])
            else:
                return True
        return False

    def DJL_containsDuplicate(self, nums):
        return False if len(nums) == len(set(nums)) else True


nums = [1, 1, 3, 3, 2, 4, 4]
nn = set(nums)


# nums.sort()
# print(nums)
# print(len(nums), len(nn))
# print(Solution().containsDuplicate(nums))


# 一个数组每个数都有一个重复的，但有一个数没有重复，找出它
def find(nums: List[int]) -> int:
    nums.sort()
    i = 0
    while i < len(nums):
        if nums[i] == nums[i + 1]:
            i += 2
        else:
            return nums[i]
    return None


print(find(nums))
