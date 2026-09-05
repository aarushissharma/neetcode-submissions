class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxDiff = 0
        new = 0
        for i in range(len(prices)):
            for j in range(i, len(prices)):
                new = prices[j] - prices[i]

                if new > maxDiff:
                    maxDiff = new

        return maxDiff