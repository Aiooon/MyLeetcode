"""
剑指 Offer 63. 股票的最大利润
假设把某股票的价格按照时间先后顺序存储在数组中，请问买卖该股票一次可能获得的最大利润是多少？

示例 1:
输入: [7,1,5,3,6,4]
输出: 5
解释: 在第 2 天（股票价格 = 1）的时候买入，在第 5 天（股票价格 = 6）的时候卖出，最大利润 = 6-1 = 5 。
注意利润不能是 7-1 = 6, 因为卖出价格需要大于买入价格。

示例 2:
输入: [7,6,4,3,1]
输出: 0
解释: 在这种情况下, 没有交易完成, 所以最大利润为 0。

限制：0 <= 数组长度 <= 10^5

date: 2021年3月7日
"""
from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        """ 
        if not prices:
            return 0
        dp = [0] * len(prices)
        for i in range(1, len(prices)):
            dp[i] = max(dp[i-1], prices[i]-min(prices[:i]))
        return max(dp) 
        
        # beats  time 6%  mem 7%
        """
        # todo 动态规划
        # beats time 96.87% mem 42.40%
        lowest, profit = float("+inf"), 0
        for price in prices:
            lowest = min(lowest, price)
            profit = max(profit, price - lowest)
        return profit


prices = [7, 1, 5, 3, 6, 4]
print(Solution().maxProfit(prices))
print(float("+inf"), float("-inf"))