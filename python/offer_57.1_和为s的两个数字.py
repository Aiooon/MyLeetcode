"""
剑指 Offer 57. 和为s的两个数字
输入一个递增排序的数组和一个数字s，在数组中查找两个数，使得它们的和正好是s。
如果有多对数字的和等于s，则输出任意一对即可。

示例 1：
输入：nums = [2,7,11,15], target = 9
输出：[2,7] 或者 [7,2]

示例 2：
输入：nums = [10,26,30,31,47,60], target = 40
输出：[10,30] 或者 [30,10]


限制：
1 <= nums.length <= 10^5
1 <= nums[i] <= 10^6

date: 2021年2月27日
"""
from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # todo 暴力解法   超时
        """ res = []
        for i in range(0, len(nums)-1):
            for j in range(i+1, len(nums)):
                if nums[i] + nums[j] == target:
                    res.append(nums[i])
                    res.append(nums[j])
                    break
            if res:
                break
        return res """

        # todo 双指针法，理由排序数组的特点
        left, right = 0, len(nums) - 1
        while left < right:
            s = nums[left] + nums[right]
            if s < target:
                left += 1
            elif s > target:
                right -= 1
            elif s == target:
                return nums[left], nums[right]
        return []

nums = [16, 16, 18, 24, 30, 32]
target = 48
print(Solution().twoSum(nums, target))
