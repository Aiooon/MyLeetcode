"""
4. 寻找两个正序数组的中位数

给定两个大小为 m 和 n 的正序（从小到大）数组 nums1 和 nums2。请你找出并返回这两个正序数组的中位数。
进阶：你能设计一个时间复杂度为 O(log (m+n)) 的算法解决此问题吗？

 
示例 1：
输入：nums1 = [1,3], nums2 = [2]
输出：2.00000
解释：合并数组 = [1,2,3] ，中位数 2

示例 2：
输入：nums1 = [1,2], nums2 = [3,4]
输出：2.50000
解释：合并数组 = [1,2,3,4] ，中位数 (2 + 3) / 2 = 2.5

示例 3：
输入：nums1 = [0,0], nums2 = [0,0]
输出：0.00000

示例 4：
输入：nums1 = [], nums2 = [1]
输出：1.00000

示例 5：
输入：nums1 = [2], nums2 = []
输出：2.00000
 
提示：
nums1.length == m
nums2.length == n
0 <= m <= 1000
0 <= n <= 1000
1 <= m + n <= 2000
-10^6 <= nums1[i], nums2[i] <= 10^6

date : 11-10-2020
"""
from typing import List


class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]):
        m, n = len(nums1), len(nums2)
        mid = (m + n) // 2
        flag = True if (m + n) % 2 else False    # 总长度是否为奇数
        merge, i, j = [], 0, 0
        if not flag:
            mid += 1
        while len(merge) <= mid:
            if nums1[i] < nums2[j] and i < m:
                merge.append(nums1[i])
                if i < m-1:
                    i += 1
                    #
                    break
            elif j < n:
                merge.append(nums2[j])
                if j < n-1:
                    j += 1
                    break
        if flag:
            return merge[-1]
        else:
            return (merge[-1]+merge[-2]) / 2



nums1 = [1, 2, 3]  # 3
nums2 = [4, 5, 6]   #
print(Solution().findMedianSortedArrays(nums1, nums2))
