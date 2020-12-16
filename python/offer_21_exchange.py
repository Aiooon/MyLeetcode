"""
剑指 Offer 21. 调整数组顺序使奇数位于偶数前面
输入一个整数数组，实现一个函数来调整该数组中数字的顺序，
使得所有奇数位于数组的前半部分，所有偶数位于数组的后半部分。

示例：
输入：nums = [1,2,3,4]
输出：[1,3,2,4]

注：[3,1,2,4] 也是正确的答案之一。

提示：
1 <= nums.length <= 50000
1 <= nums[i] <= 10000

date : 12-16-2020
"""
from typing import List


class Solution:
    def exchange(self, nums: List[int]) -> List[int]:
        """
        思路：
        实现 partition 函数，划分依据为奇数在左半边，偶数在右半边
        :param nums:
        :return:
        """
        if not nums:
            return []
        pos = 0
        # 找到第一个偶数的位置
        while pos < len(nums):
            if nums[pos] % 2:
                pos += 1
            else:
                break
        for i in range(pos + 1, len(nums)):
            if nums[i] % 2:
                nums[pos], nums[i] = nums[i], nums[pos]
                pos += 1
        return nums


if __name__ == '__main__':
    nums = [1, 2, 3, 4, 5]
    print(Solution().exchange(nums))
