class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit, l = 0, 0
        
        for r in range(len(prices)):
            if prices[r] - prices[l] > profit:
                profit = prices[r] - prices[l]
            if prices[r] < prices[l]:
                l = r
                
        return profit
            