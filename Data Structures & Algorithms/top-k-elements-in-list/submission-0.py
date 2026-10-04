class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        amt = defaultdict(int)
        ret = []
        for i in range(len(nums)):
            amt[nums[i]] += 1
            
        for j in range(k):
            most_frequent = max(amt, key=amt.get)
            ret.append(most_frequent)

            del amt[most_frequent]            
        return ret