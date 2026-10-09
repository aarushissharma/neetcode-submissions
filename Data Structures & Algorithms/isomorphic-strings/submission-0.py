class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        mapST, mapTS = {}, {}

        for i, n in enumerate(s):
            mapST[n] = t[i]
        for j, c in enumerate(t):
            mapTS[c] = s[j]

        print(mapTS.values())
        print(mapST.keys())

        return list(mapTS.keys()) == list(mapST.values())