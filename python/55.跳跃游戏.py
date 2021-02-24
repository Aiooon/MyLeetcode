#
# @lc app=leetcode.cn id=55 lang=python3
#
# [55] 跳跃游戏
#

# @lc code=start
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        """
        思路：
        尽可能到达最远位置（贪心）。
        如果能到达某个位置，那一定能到达它前面的所有位置。

        Args:
            nums (List[int]): [description]

        Returns:
            bool: [description]
        """

        furthest = 0
        for i, step in enumerate(nums):
            if i > furthest:
                return False
            furthest = max(furthest, i + step)
        return True
# @lc code=end

