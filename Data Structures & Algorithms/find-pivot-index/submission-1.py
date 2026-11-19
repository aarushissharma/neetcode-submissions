class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        sides = {}
        left = 0
        right = sum(nums)
        for i in range(len(nums)):
            # diff of left & right : index of num
            right -= nums[i]
            sides[left-right] = i
            if left - right == 0:
                return i
            left += nums[i]
            
        
        return sides.get(0, -1)

