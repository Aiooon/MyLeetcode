from typing import List


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        """
        给定一个未排序的整数数组，找出最长连续序列的长度。要求算法的时间复杂度为 O(n)。

        示例:
            输入: [100, 4, 200, 1, 3, 2]
            输出: 4
        解释:
            最长连续序列是 [1, 2, 3, 4]。它的长度为 4。

        :param nums:
        :return:
        """
        if not nums:
            return 0
        num_set = list(set(nums))
        max_len = 1
        for num in num_set:
            if num - 1 in nums:
                continue
            cur_num = num
            cur_len = 1
            while cur_num + 1 in num_set:
                    cur_num += 1
                    cur_len += 1
            max_len = max(max_len, cur_len)

        return max_len


nums = [-903,-904,-905,-906,-907,-908,-909,-910,-911,-912,-913,-914,-915,-916,-917,-918,-919,-920,-921,-922,-923,-924,-925,-926,-927,-928,-929,-930,-931,-932,-933,-934,-935,-936,-937,-938,-939,-940,-941,-942,-943,-944,-945,-946,-947,-948,-949,-950,-951,-952,-953,-954,-955,-956,-957,-958,-959,-960,-961,-962,-963,-964,-965,-966,-967,-968,-969,-970,-971,-972,-973,-974,-975,-976,-977,-978,-979,-980,-981,-982,-983,-984,-985,-986,-987,-988,-989,-990,-991,-992,-993,-994,-995,-996,-997,-998,-999]
s = Solution()
print(s.longestConsecutive(nums))