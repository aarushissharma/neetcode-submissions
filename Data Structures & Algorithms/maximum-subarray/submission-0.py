class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        net = [0] * len(nums)
        net[0] = nums[0]
        
        for i in range(1, len(nums)):
            if net[i-1] + nums[i] > nums[i]:
                net[i] = net[i-1] + nums[i]
            else:
                net[i] = nums[i]

        return max(net)