class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        letS, letT= {}, {}
        for i, c in enumerate(s):
            letS[c] = letS.get(c, 0) + 1
            letT[t[i]] = letT.get(t[i], 0) + 1
        
        return letS == letT


        