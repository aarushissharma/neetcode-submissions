class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        diff, l = 0, 0
        letters = set()
        for r in range(len(s)):
            while s[r] in letters:
                letters.remove(s[l])
                l += 1
            diff = max(diff, r-l+1)
            letters.add(s[r])
        
        return diff
