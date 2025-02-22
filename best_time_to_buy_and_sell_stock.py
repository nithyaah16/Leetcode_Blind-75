class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        min_price = prices[0]
        max_profit = 0
        
        for i in prices:
            if i < min_price:
                min_price = i
            profit = i - min_price
            if profit > max_profit:
                max_profit = profit
        return max_profit
