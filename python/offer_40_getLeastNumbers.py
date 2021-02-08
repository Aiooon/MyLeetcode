"""
剑指 Offer 40. 最小的k个数
输入整数数组 arr ，找出其中最小的 k 个数。例如，输入4、5、1、6、2、7、3、8这8个数字，则最小的4个数字是1、2、3、4。

示例 1：
输入：arr = [3,2,1], k = 2
输出：[1,2] 或者 [2,1]

示例 2：
输入：arr = [0,1,2,1], k = 1
输出：[0]

限制：
0 <= k <= arr.length <= 10000
0 <= arr[i] <= 10000

date : 2-1-2021
"""
from typing import List


class Solution:
    def getLeastNumbers(self, arr: List[int], k: int) -> List[int]:
        if len(arr) <= 1:
            return arr[:k]
        return self.quick_sort(arr, 0, len(arr)-1, k)

    def quick_sort(self, nums, left, right, k):
        if left < right:
            pos = self.partition(nums, left, right)
            if pos == k:
                return nums[:pos]
            elif pos < k:
                return self.quick_sort(nums, left, pos, k)
            else:
                return self.quick_sort(nums, pos+1, right, k)

    def partition(self, nums, left, right):
        pivot, fin_pos = nums[left], left
        for i in range(left + 1, right + 1):
            if nums[i] < pivot:
                fin_pos += 1
                nums[i], nums[fin_pos] = nums[fin_pos], nums[i]
        nums[left], nums[fin_pos] = nums[fin_pos], nums[left]
        return fin_pos


if __name__ == '__main__':
    arr = [0, 1, 2, 1]
    k = 2
    print(Solution().getLeastNumbers(arr, k))
