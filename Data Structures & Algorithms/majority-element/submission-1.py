class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        # number of times that element is seen: actual element

        count = {}

        for i in range(len(nums)):
            count[nums[i]] = count.get(nums[i], 0) + 1
        
        for c in count:
            if count.get(c, 0) >= (len(nums)/2-1):
                return c