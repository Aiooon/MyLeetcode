"""
503. 下一个更大元素 II
给定一个循环数组（最后一个元素的下一个元素是数组的第一个元素），输出每个元素的下一个更大元素。
数字 x 的下一个更大的元素是按数组遍历顺序，这个数字之后的第一个比它更大的数，
这意味着你应该循环地搜索它的下一个更大的数。如果不存在，则输出 -1。

示例 1:

输入: [1,2,1]
输出: [2,-1,2]
解释: 第一个 1 的下一个更大的数是 2；
数字 2 找不到下一个更大的数； 
第二个 1 的下一个最大的数需要循环搜索，结果也是 2。
注意: 输入数组的长度不会超过 10000。

date: 2021年3月6日
"""

from typing import List


class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        # 暴力法  时间O(n^2) 空间O(n)
        """ def findGreater(n, nums):
            for num in nums:
                if num > n:
                    return num
            return None

        l = len(nums)
        res = []
        for i in range(l):
            before, after = nums[:i], nums[i+1:]
            afg = findGreater(nums[i], after)
            beg = findGreater(nums[i], before)
            if afg is not None:
                res.append(afg)
            elif beg is not None:
                res.append(beg)
            else:
                res.append(-1)
        return res """

        # todo 单调栈 栈中存的是数组元素下标
        """
        要从逻辑上去理解为什么能用「单调栈」解决问题：
        1.我们希望将 O(n^2) 算法优化为 O(n) 算法，因此需要将「主动」获取答案转换为「被动」更新
        2.我们需要使用数据结构保持那些「尚未更新」的位置下标，由于题目要求的是找「下一个更大的元素」，因此使用栈来保存
        3.「被动」更新答案的逻辑导致了我们栈内元素单调

        单调栈的可以做到 O(n) 的复杂度，我们将当前还没得到答案的下标暂存于栈内，从而实现「被动」更新答案。
        也就是说，栈内存放的永远是还没更新答案的下标。

        由于我们要找每一个元素的下一个更大的值，因此我们需要对原数组遍历两次，对遍历下标进行取余转换。
        以及因为栈内存放的是还没更新答案的下标，可能会有位置会一直留在栈内（最大值的位置），因此我们要在处理前预设答案为 -1。
        而从实现那些没有下一个更大元素（不出栈）的位置的答案是 -1。
        """
        l = len(nums)
        res = [-1] * l
        stack = []
        for i in range(l * 2):      # 实现循环数组 遍历两次 取模
            while stack and nums[stack[-1]] < nums[i % l]:
                res[stack.pop()] = nums[i % l]
            stack.append(i % l)
        return res

nums = [1,2,1]
print(Solution().nextGreaterElements(nums))