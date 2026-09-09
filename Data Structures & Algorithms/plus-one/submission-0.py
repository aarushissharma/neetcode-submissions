class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        start = 0
        place = 0
        for i in range(len(digits)-1, -1, -1):
            start += digits[i] * (10 ** place)
            place += 1
        
        start += 1
        
        new = [int(num) for num in str(start)]

        return new
