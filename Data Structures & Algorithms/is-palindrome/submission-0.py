class Solution:
    def isPalindrome(self, s: str) -> bool:
        #disregard  spaces (cannot be case sensitive)
        # 1 pointer at front, 2nd in the back 
        #for 1/2 of the lenth of the string:
        #   pointer at one end has to match pointer at the other
        #   if they don't, then return false
        # at the end return true

        new = ""
        for i in s:
            if i.isalnum():
                new += i.lower()

        return new == new[::-1];

        