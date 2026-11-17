class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        diffs = [0]

        for i in range(1, len(prices)):
             diffs.append(prices[i] - min(prices[:i]))
        return max(diffs)