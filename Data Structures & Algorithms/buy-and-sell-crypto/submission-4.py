class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        delta, l, r = 0, 0, 1

        while r < len(prices):
            if prices[l] < prices[r]:
                diff = prices[r] - prices[l]
                delta = max(delta, diff)
            else:
                l = r
            r += 1
        return delta
            
        