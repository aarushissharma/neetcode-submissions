class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        all = []
        nums = sorted(nums)
        for i in range(nums[-1]+1):
            if nums[i] != i:
                return i
        return(len(nums))


            