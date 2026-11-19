class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices: return 0
        max_profit = 0
        max_price = prices[-1]

        for i in range(len(prices)-1,-1,-1):
            curr_price = prices[i]
            
            profit = max_price - curr_price

            max_price = max(max_price,curr_price)
            max_profit = max(max_profit,profit)
        return max_profit