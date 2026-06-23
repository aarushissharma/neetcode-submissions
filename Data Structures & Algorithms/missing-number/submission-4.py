class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        nums.sort()
        max_index = len(nums)


        for i in range(0, max_index):
            if nums[i] != i:
                return i
            if len(nums) not in nums:
                return len(nums)