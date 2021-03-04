"""
354. 俄罗斯套娃信封问题
给定一些标记了宽度和高度的信封，宽度和高度以整数对形式 (w, h) 出现。
当另一个信封的宽度和高度都比这个信封大的时候，这个信封就可以放进另一个信封里，如同俄罗斯套娃一样。
请计算最多能有多少个信封能组成一组“俄罗斯套娃”信封（即可以把一个信封放到另一个信封里面）。

说明:
不允许旋转信封。

示例:

输入: envelopes = [[5,4],[6,4],[6,7],[2,3]]
输出: 3 
解释: 最多信封的个数为 3, 组合为: [2,3] => [5,4] => [6,7]。

date: 2021年3月4日
"""
from typing import List


class Solution:
    def maxEnvelopes(self, envelopes: List[List[int]]) -> int:
        # todo  一维升序 二维降序排序，在第二维找最长递增子序列
        if not envelopes:
            return 0
        envelopes.sort(key=lambda x: (x[0], -x[1]))

        heights = []     # 高度数组
        for i in range(len(envelopes)):
            heights.append(envelopes[i][1])

        # 找出最长递增子序列长度   第300题
        tails, res = [0]*len(heights), 0
        for num in heights:
            i, j = 0, res
            while i < j:
                m = (i + j) // 2
                if tails[m] < num:
                    i = m + 1
                else:
                    j = m
            tails[i] = num
            if j == res:
                res += 1

        return res


envelopes = [[2, 100], [3, 200], [4, 300], [5, 500],
             [5, 400], [5, 250], [6, 370], [6, 360], [7, 380]]
print(Solution().maxEnvelopes(envelopes))
# envelopes.sort()
# print(envelopes)
