class Solution:
    def isPalindrome(self, s: str) -> bool:
        raw = []

        for c in s:
            if c.isalnum():
                raw.append(c.lower())
        l, r = 0, len(raw)-1
        while l < r:
            if raw[l] == raw[r]:
                l += 1
                r -= 1
            else:
                return False
        return True