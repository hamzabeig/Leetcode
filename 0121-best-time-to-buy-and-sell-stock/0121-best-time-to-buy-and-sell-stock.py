# class Solution:
#     def maxProfit(self, prices: List[int]) -> int:
#         maxP = 0
#         l =0
#         r = 1
#         while r < len(prices):
#             if prices[r] > prices[l]:
#                 maxP= max(maxP, prices[r]-prices[l])
                
#             else:
#                 l=r
#             r+=1
#         return maxP



class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        min_price = float('inf')
        max_profit = 0
        for price in prices:
            if price < min_price:
                min_price = price  
            elif price - min_price > max_profit:
                max_profit = price - min_price   
        
        return max_profit
