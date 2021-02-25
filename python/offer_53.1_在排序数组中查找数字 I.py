"""
剑指 Offer 53 - I. 在排序数组中查找数字 I
统计一个数字在排序数组中出现的次数。

示例 1:
输入: nums = [5,7,7,8,8,10], target = 8
输出: 2

示例 2:
输入: nums = [5,7,7,8,8,10], target = 6
输出: 0


限制：0 <= 数组长度 <= 50000

注意：本题与主站 34 题相同（仅返回值不同）：https://leetcode-cn.com/problems/find-first-and-last-position-of-element-in-sorted-array/

date: 2021年2月25日
"""

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # todo 排序数组中的搜索问题，首先想到 二分法 解决。
        count = 0
        for num in nums:
            if num == target:
                count += 1
            if num > target:
                break
        return count