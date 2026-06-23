class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        '''
        go through whole list
        copy number to a set
        if a certain number is in the set already then delete it from the set
        return the set[0]
        '''
        myArray = []
        nums.sort()
        for i in range(len(nums)-1):
            if nums[i] == nums[i+1]:
                nums[i] = None
                nums[i+1] = None
        for j in range(len(nums)):
            if nums[j] != None:
                return nums[j]

        