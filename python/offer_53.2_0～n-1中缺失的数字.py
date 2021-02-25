"""
剑指 Offer 53 - II. 0～n-1中缺失的数字
一个长度为n-1的递增排序数组中的所有数字都是唯一的，并且每个数字都在范围0～n-1之内。
在范围0～n-1内的n个数字中有且只有一个数字不在该数组中，请找出这个数字。

示例 1:
输入: [0,1,3]
输出: 2

示例 2:
输入: [0,1,2,3,4,5,6,7,9]
输出: 8

[0,1,3,4,5,6,7,8,9]

限制：1 <= 数组长度 <= 10000

date: 2021年2月25日
"""
from typing import List

class Solution:
    def missingNumber(self, nums: List[int]):
        # todo 排序数组中的搜索问题，首先想到 二分法 解决
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = (left + right) // 2
            # 如果 nums[mid] == mid 说明缺的数在右边 
            if nums[mid] == mid:
                left = mid + 1
            # 如果 nums[mid] > mid 说明缺的数在左边 
            else:
                right = mid - 1
        return left


nums = [0,1,2,3,4,5,6,7,9]
print(Solution().missingNumber(nums))
