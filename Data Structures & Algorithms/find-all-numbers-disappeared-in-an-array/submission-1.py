class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        out = []
        for i in range(1, len(nums)+1):
            if i not in nums:
                out.append(i)
        return out
        