"""
300. 最长递增子序列
给你一个整数数组 nums ，找到其中最长严格递增子序列的长度。
子序列是由数组派生而来的序列，删除（或不删除）数组中的元素而不改变其余元素的顺序。
例如，[3,6,2,7] 是数组 [0,3,1,6,2,2,7] 的子序列。

示例 1：
输入：nums = [10,9,2,5,3,7,101,18]
输出：4
解释：最长递增子序列是 [2,3,7,101]，因此长度为 4 。

示例 2：
输入：nums = [0,1,0,3,2,3]
输出：4

示例 3：
输入：nums = [7,7,7,7,7,7,7]
输出：1

提示：
1 <= nums.length <= 2500
-104 <= nums[i] <= 10^4

进阶：
你可以设计时间复杂度为 O(n2) 的解决方案吗？
你能将算法的时间复杂度降低到 O(n log(n)) 吗?

date: 2021年3月4日
"""
from typing import List

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        # todo 动态规划 + 二分
        tails, res = [0] * len(nums), 0
        for num in nums:
            i, j = 0, res
            while i < j:
                m = (i + j) // 2
                if tails[m] < num:  # 如果要求非严格递增，将此行 '<' 改为 '<=' 即可。
                    i = m + 1  
                else:
                    j = m
            tails[i] = num
            if j == res:
                res += 1
        return res


nums = [10, 9, 2, 5, 3, 7, 101, 18]
print(Solution().lengthOfLIS(nums))
