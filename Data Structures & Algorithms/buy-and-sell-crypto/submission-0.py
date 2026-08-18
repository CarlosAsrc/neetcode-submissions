class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_p = prices[0]
        profit = 0
        for i, p in enumerate(prices[1:]):
            profit = max(p - min_p, profit)
            min_p = min_p if min_p < p else p
        return max(profit, 0)


        