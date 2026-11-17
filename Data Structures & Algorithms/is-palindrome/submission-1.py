class Solution:
    def isPalindrome(self, s: str) -> bool:
        all = []
        for c in s:
            if c.isalnum():
                all.append(c.lower())

        return(all==all[::-1])