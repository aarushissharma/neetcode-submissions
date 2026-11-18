class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # need to check what the max diff is
        l, diff = 0, 0
        seen = set()
        for r in range(len(s)):
            while s[r] in seen:
                seen.remove(s[l])
                l += 1
            diff = max(diff, r-l+1)
            seen.add(s[r])
        return diff