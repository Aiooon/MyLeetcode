"""
1128. 等价多米诺骨牌对的数量
给你一个由一些多米诺骨牌组成的列表 dominoes。
如果其中某一张多米诺骨牌可以通过旋转 0 度或 180 度得到另一张多米诺骨牌，我们就认为这两张牌是等价的。
形式上，dominoes[i] = [a, b] 和 dominoes[j] = [c, d]
等价的前提是 a==c 且 b==d，或是 a==d 且 b==c。

在 0 <= i < j < dominoes.length 的前提下，
找出满足 dominoes[i] 和 dominoes[j] 等价的骨牌对 (i, j) 的数量。


示例：
输入：dominoes = [[1,2],[2,1],[3,4],[5,6]]
输出：1

提示：
1 <= dominoes.length <= 40000
1 <= dominoes[i][j] <= 9

date : 1-26-2021
"""
from typing import List


class Solution:
    def numEquivDominoPairs(self, dominoes: List[List[int]]):
        """
        遍历列表，当找到 i 和 j 位置构成等价时，将位置对 (i,j)加入集合 res
        返回 res 的长度
        :param dominoes:
        :return:
        """
        if len(dominoes) <= 1:
            return 0
        nums = [0] * 100
        res = 0
        for x, y in dominoes:
            num = x * 10 + y if x <= y else y * 10 + x
            res += nums[num]
            nums[num] += 1
        return res


if __name__ == '__main__':
    dominoes = [[1, 2], [1, 2], [1, 2], [2, 1]]
    print(Solution().numEquivDominoPairs(dominoes))
