"""
338. 比特位计数
给定一个非负整数 num。对于 0 ≤ i ≤ num 范围中的每个数字 i ，
计算其二进制数中的 1 的数目并将它们作为数组返回。

示例 1:
输入: 2
输出: [0,1,1]

示例 2:
输入: 5
输出: [0,1,1,2,1,2]

进阶:
1.给出时间复杂度为O(n*sizeof(integer))的解答非常容易。
  但你可以在线性时间O(n)内用一趟扫描做到吗？
2.要求算法的空间复杂度为O(n)。
3.你能进一步完善解法吗？要求在C++或任何其他语言中不使用任何内置函数
 （如 C++ 中的 __builtin_popcount）来执行此操作。

date: 2021年3月3日
"""
from typing import List


class Solution:
    def countBits(self, num: int) -> List[int]:
        # todo 判断奇偶性
        """ res = [0] * (num + 1)
        for i in range(1, num + 1):
            if i % 2:
                res[i] = res[i-1] + 1
            else:
                res[i] = res[i//2]
        return res """

        # todo  动态规划
        res = [0] * (num + 1)
        for i in range(1, num + 1):
            res[i] = res[i >> 1] + (i & 1)    # 右移一位  加上最低位是否是 1
        return res


num = 5   # 101
print(Solution().countBits(num))
