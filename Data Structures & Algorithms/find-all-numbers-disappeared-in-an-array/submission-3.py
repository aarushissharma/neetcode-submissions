class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        ideal = set()
        out = []
        for i in range(1, len(nums)+1):
            ideal.add(i)
        for n in ideal:
            if n not in nums:
                out.append(n)
        return out
