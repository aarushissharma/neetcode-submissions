class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:

        single = set()

        for i in range(1, len(nums)+1):
            single.add(i)
        for n in nums:
            single.discard(n)
        return list(single)           
        