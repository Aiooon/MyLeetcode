"""
剑指 Offer 61. 扑克牌中的顺子
从扑克牌中随机抽5张牌，判断是不是一个顺子，即这5张牌是不是连续的。
2～10为数字本身，A为1，J为11，Q为12，K为13，而大、小王为 0 ，可以看成任意数字。
A 不能视为 14。

示例 1:
输入: [1,2,3,4,5]
输出: True

示例 2:
输入: [0,0,1,2,5]
输出: True

限制：
数组长度为 5 
数组的数取值为 [0, 13]

date: 2021年2月28日
"""
from typing import List


class Solution:
    def isStraight(self, nums: List[int]) -> bool:
        if len(nums) != 5:
            return False
        nums.sort()
        laizi = 0
        for i in range(len(nums)):
            if nums[i] < 0 or nums[i] > 13:
                return False
            if nums[i] == 0:
                laizi += 1
            elif i > 0:
                if nums[i] == nums[i-1]+1:
                    continue
                elif nums[i] > nums[i-1]+1:
                    if nums[i-1] == 0:
                        continue
                    elif laizi >= nums[i] - nums[i-1] - 1:
                        continue
                    else:
                        return False
                else:
                    return False
            else:
                continue
        return True

        # todo 满足条件 1.除大小王外无重复 2. ma-mi<5
        # 集合set + 遍历
        """ repeat = set()
        ma, mi = 0, 14
        for num in nums:
            if num == 0:
                continue
            mi = min(mi, num)
            ma = max(ma, num)
            if num in repeat:
                return False
            repeat.add(num)
        return ma-mi < 5 """

        # 排序 + 遍历
        joker = 0
        nums.sort() # 数组排序
        for i in range(4):
            if nums[i] == 0: joker += 1 # 统计大小王数量
            elif nums[i] == nums[i + 1]: return False # 若有重复，提前返回 false
        return nums[4] - nums[joker] < 5 # 最大牌 - 最小牌 < 5 则可构成顺子


nums = [0, 0, 8, 5, 4]
print(Solution().isStraight(nums))
# nums.sort()
# print(nums)
