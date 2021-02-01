"""
剑指 Offer 39. 数组中出现次数超过一半的数字
数组中有一个数字出现的次数超过数组长度的一半，请找出这个数字。
你可以假设数组是非空的，并且给定的数组总是存在多数元素。

示例 1:
输入: [1, 2, 3, 2, 2, 2, 5, 4, 2]
输出: 2

限制：
1 <= 数组长度 <= 50000

date : 2-1-2021
"""
from typing import List


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = {}
        for num in nums:
            if str(num) not in count:
                count[str(num)] = 1
            else:
                count[str(num)] += 1
        for key in count:
            if count[key] > len(nums) / 2:
                return int(key)

    def sort(self, nums: List[int]) -> int:
        nums.sort()
        return nums[len(nums)//2]

    def vote(self, nums: List[int]) -> int:
        votes, count = 0, 0
        x = nums[0]
        for num in nums:
            if votes == 0:
                x = num
            votes += 1 if num == x else -1
        for num in nums:
            if num == x:
                count += 1
        return x if count > len(nums)//2 else 0


if __name__ == '__main__':
    nums = [1, 2, 3, 2, 2, 2, 5, 4, 2]
    print(Solution().majorityElement(nums))
    print(Solution().sort(nums))
    print(Solution().vote(nums))

