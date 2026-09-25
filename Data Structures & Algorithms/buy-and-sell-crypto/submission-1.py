class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        delta = 0 
        for i in range(len(prices)):
            for j in range(i, len(prices)):
                diff = prices[j] - prices[i]
                if diff > delta:
                    delta = diff
        return delta
