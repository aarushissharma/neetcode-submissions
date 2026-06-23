class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_list = list()
        for i in range(len(nums)):
            difference = target - nums[i]
            for j in range(i+1, len(nums)):
                if(i != j):
                    if(nums[j] == difference):
                        num_list.append(i)
                        num_list.append(j)
        return num_list
                    