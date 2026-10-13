class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l, r, delta = 0, 1, 0

        while r < len(prices):
            if prices[l] < prices[r]:
                diff = prices[r] - prices[l]
                delta = max(diff, delta)
            else:
                l = r
            r += 1
        return delta
