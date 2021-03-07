"""
剑指 Offer 66. 构建乘积数组
给定一个数组 A[0,1,…,n-1]，请构建一个数组 B[0,1,…,n-1]，
其中 B[i] 的值是数组 A 中除了下标 i 以外的元素的积, 即 B[i]=A[0]×A[1]×…×A[i-1]×A[i+1]×…×A[n-1]。
不能使用除法。

示例:
输入: [1,2,3,4,5]
输出: [120,60,40,30,24]


提示：
所有元素乘积之和不会溢出 32 位整数
a.length <= 100000

date: 2021年3月7日
"""
from typing import List

class Solution:
    def constructArr(self, a: List[int]) -> List[int]:
        """
        思路:
        结果集中任何一个元素 = 其左边所有元素的乘积 * 其右边所有元素的乘积。
        一轮循环:构建左边的乘积并保存在结果集中，
        二轮循环:构建右边乘积，乘以左边的乘积，并将最终结果保存

        Args:
            a (List[int]): [description]

        Returns:
            List[int]: [description]
        """
        b = [1] * len(a)
        tmp = 1
        for i in range(1, len(a)):      # 计算下三角
            b[i] = b[i - 1] * a[i - 1]
        for i in range(len(a) - 2, -1, -1):     # 计算上三角
            tmp *= a[i + 1]
            b[i] *= tmp     # 下三角 * 上三角
        return b



print(Solution().constructArr([1,2,3,4,5]))