class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        out = []
        nums = sorted(nums)

        for n in range(len(nums)):
            if (n > 0) and (nums[n] == nums[n-1]):
                continue
            l, r = n+1, len(nums)-1 
            while l < r:
                tot = nums[n] + nums[r] + nums[l]
                if tot < 0:
                    l += 1
                elif tot > 0:
                    r -= 1
                else:
                    out.append([nums[n], nums[l], nums[r]])
                    l += 1
                    while (l < r) and (nums[l] == nums[l-1]):
                        l += 1
        return out