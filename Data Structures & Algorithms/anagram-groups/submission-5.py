class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # each word should be counted with a hashmap and then returned if there is an equivalent
        vals = {}
        # key is the hashmap of letters
        ret = []
        
        for s in strs:
            alph = [0] * (26)
            for l in s:
                #logic to add stuff to the alph string
                alph[ord(l)- ord('a')] += 1
            key = str(alph)
            
            if key not in vals:
                vals[key] = []
            vals[key].append(s)
        return list(vals.values())
            

        print(alph)