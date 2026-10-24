class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        prevMap = {}
        # value needed: key to match


        for i, n in enumerate(nums):
            if n in prevMap:
                return [prevMap[n], i]

            prevMap[target - n] = i

        
