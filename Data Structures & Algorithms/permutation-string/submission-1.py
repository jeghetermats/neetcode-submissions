class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        freq1 = {}
        for c in s1:
            freq1[c] = freq1.get(c,0)+1
        freq2 = {}

        l=0
        for r in range(len(s2)):
            c = s2[r]
            freq2[c] = freq2.get(c,0)+1
            while freq2.get(c,0)>freq1.get(c,0):
                freq2[s2[l]]-=1
                if freq2[s2[l]] ==0:
                    del freq2[s2[l]]
                l+=1
            if freq1 == freq2:
                return True
        return False