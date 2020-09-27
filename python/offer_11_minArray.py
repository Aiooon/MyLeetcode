"""
剑指 Offer 11. 旋转数组的最小数字
把一个数组最开始的若干个元素搬到数组的末尾，我们称之为数组的旋转。
输入一个递增排序的数组的一个旋转，输出旋转数组的最小元素。
例如，数组 [3,4,5,1,2] 为 [1,2,3,4,5] 的一个旋转，该数组的最小值为1。

示例 1：

输入：[3,4,5,1,2]
输出：1
示例 2：

输入：[2,2,2,0,1]
输出：0

date : 9-27-2020
"""
from typing import List


class Solution:
    # Perfect code
    def minArray_(self, numbers: [int]) -> int:
        i, j = 0, len(numbers) - 1
        while i < j:
            m = (i + j) // 2
            if numbers[m] > numbers[j]:
                i = m + 1
            elif numbers[m] < numbers[j]:
                j = m
            else:
                j -= 1
        return numbers[i]

    def minArray(self, numbers: List[int]) -> int:
        if not numbers:
            return 0
        if len(numbers) == 1:
            return numbers[0]
        left, mid, right = 0, 0, len(numbers)-1

        while numbers[left] >= numbers[right]:
            if right - left == 1:
                mid = right
                break
            mid = (left + right) // 2
            if numbers[left] == numbers[mid] == numbers[right]:
                return self.minInOrder(numbers, left, right)

            if numbers[mid] >= numbers[left]:
                left = mid
            elif numbers[mid] <= numbers[right]:
                right = mid

        return numbers[mid]

    def minInOrder(self, numbers, left, right):
        res = numbers[left]
        for i in range(left, right):
            if res > numbers[i]:
                res = numbers[i]
        return res


sol = Solution()
# nums = [10, 1, 10, 10, 10]
# nums = [1, 3, 5]
# nums = [1, 0, 1, 1, 1]
nums = [1, 1, 1, 0, 1]

# print(sol.minArray(nums))
print(sol.minArray_(nums))

