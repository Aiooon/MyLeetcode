#
# @lc app=leetcode.cn id=122 lang=python3
#
# [122] 买卖股票的最佳时机 II
#

# @lc code=start
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        res = 0
        for i in range(1, len(prices)):
            # 价格上涨时等价于每天都交易
            res += max(0, prices[i] - prices[i - 1])
        return res
# @lc code=end
