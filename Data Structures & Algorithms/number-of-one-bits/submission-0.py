class Solution:
    def hammingWeight(self, n: int) -> int:
        bit = 0
        for i in range(32, -1, -1):
            pow = i
            if n >= (2 ** pow):
                n -= 2 ** pow
                bit += 1
        return bit
            
