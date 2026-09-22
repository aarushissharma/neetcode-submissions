class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = []
        zeros = 0
        totalProd = 1

        for i in range(len(nums)):
            if nums[i] == 0:
                zeros += 1
            else:
                totalProd *= nums[i]

        for l in range(len(nums)):
            if zeros >= 2:
                res.append(0)
            
            if zeros == 1:
                if nums[l] == 0:
                    res.append(int(totalProd))
                else: 
                    res.append(0)
            if zeros == 0:
                res.append(int(totalProd / nums[l]))
        return res
