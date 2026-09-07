class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l = 0
        gmin = prices[0]
        res = 0
        for r in range(len(prices)):
            if prices[r] < prices[l]:
                gmin = prices[r]
                l = r
            res = max(res, prices[r] -gmin)
        return res



        