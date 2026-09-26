class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        
        total = 0 
        res = float('inf')
        l = 0
        for r, n in enumerate(nums):
            total += n
            while total >= target:
                res = min(r - l + 1, res)
                total -= nums[l]
                l += 1
            
        return 0 if res == float("inf") else res
         

        

