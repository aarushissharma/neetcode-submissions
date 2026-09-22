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
        
        if zeros >= 2:
            for l in range(len(nums)):
                res.append(0)
            return res
        if zeros == 1:
            for p in range(len(nums)):
                if nums[p] == 0:
                    res.append(int(totalProd))
                else: 
                    res.append(0)
        if zeros == 0:
            for z in range(len(nums)):
                res.append(int(totalProd / nums[z]))
        return res



        
