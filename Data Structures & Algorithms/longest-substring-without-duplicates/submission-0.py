class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0

        longest, first, last = 1, 0, 0

        while last != len(s) - 1:
            last += 1

            dup = s.find(s[last], first, last)
            if dup != -1:
                first = dup + 1

            longest = max(last - first + 1, longest)
        return longest