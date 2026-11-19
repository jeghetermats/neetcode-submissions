class Solution:
    def minWindow(self, s: str, t: str) -> str:
        found = False
        shortest = (0,0,float("inf"))
        freqt = {}
        for i in t:
            freqt[i] = freqt.get(i,0)+1
        freqs = {}

        l = 0
        for r in range(len(s)):
            c = s[r]
            freqs[c] = freqs.get(c,0)+1
            f = True
            for char, freq in freqt.items():
                if freq <= freqs.get(char,0):
                    pass
                else:
                    f = False
                    break
            if f:
                found = True
                while True:
                    remove_c = s[l]
                    if remove_c in freqt and freqs[remove_c] == freqt[remove_c]:
                        break                      
                    freqs[remove_c] -= 1
                    l += 1
                if r - l + 1 < shortest[2]:
                    shortest = (l, r, r - l + 1)

        return s[shortest[0]:shortest[1]+1] if found else ""

