class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        

        # value neede: key of num
        prevMap = {}
        for i, n in enumerate(nums):
            if n in prevMap:
                return[prevMap[n], i]
            prevMap[target - n] = i
            


        print(prevMap)
            