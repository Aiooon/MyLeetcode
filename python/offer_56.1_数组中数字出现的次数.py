"""
剑指 Offer 56 - I. 数组中数字出现的次数
一个整型数组 nums 里除两个数字之外，其他数字都出现了两次。
请写程序找出这两个只出现一次的数字。要求时间复杂度是O(n)，空间复杂度是O(1)。

示例 1：
输入：nums = [4,1,4,6]
输出：[1,6] 或 [6,1]

示例 2：
输入：nums = [1,2,10,4,1,4,3,3]
输出：[2,10] 或 [10,2]

限制：2 <= nums.length <= 10000

date: 2021年2月27日
"""
from typing import List


class Solution:
    def singleNumbers(self, nums: List[int]) -> List[int]:
        # 遍历+哈希表  时间O(N) 空间O(N) 不符合
        """ dic = {}
        for num in nums:
            if num in dic:
                dic[num] = False
            else:
                dic[num] = True
        res = []
        for key, val in dic.items():
            if val:
                res.append(key)
        return res """

        # todo 分组位运算
        m, n, x, y = 1, 0, 0, 0
        """
        m 记录 n 中第一个1的位置
        n 记录数组中所有数据异或运算后的结果，即 x^y
        x, y 分别表示两个只出现了一次的数
        """
        for num in nums:    # 遍历异或，计算 x^y
            n ^= num
        while n & m == 0:   # 循环左移，找到第一个 1 的位置
            m <<= 1
        for num in nums:    # 分组
            if num & m:
                x ^= num
            else:
                y ^= num
        return x, y


nums = [1, 2, 10, 4, 1, 4, 3, 3]
# x = 0
# for num in nums:  # 1. 遍历 nums 执行异或运算
#     x ^= num
#     print(x)
print(Solution().singleNumbers(nums))

