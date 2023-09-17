#https://leetcode.com/problems/best-time-to-buy-and-sell-stock
#First try solution, I believe this works but time limit exceeded
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price, max_price = prices[0], prices[len(prices) - 1]
        min_day, max_day = 0, len(prices) - 1
        
        for index in range(len(prices)):
            if prices[index] < min_price and index < max_day:
                min_price = prices[index]
                min_day = index
            elif prices[index] < min_price:
                remaining_max = max(prices[index:]) 
                if remaining_max - prices[index] > max_price - min_price:
                    min_price = prices[index]
                    min_day = index
                    max_price = prices[len(prices) - 1]
                    max_day = len(prices) - 1
            elif prices[index] > max_price and index > min_day:
                max_price = prices[index]
                max_day = index
            
        difference = max_price - min_price

        if difference > 0:
            return difference
        else:
            return 0