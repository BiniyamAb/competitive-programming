from ast import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit, least = 0, prices[0]
        for price in prices:
            profit = max(profit, price - least)
            least = min(least, price)
        
        return profit