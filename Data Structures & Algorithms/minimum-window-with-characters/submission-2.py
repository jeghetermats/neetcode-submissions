class Solution:
    def minWindow(self, s: str, t: str) -> str:
        found = False
        shortest = (0,len(s))
        freq_t = {}
        for c in t:
            freq_t[c] = freq_t.get(c,0)+1
        max_matching = len(freq_t)

        l = 0
        matching = 0
        freq_s = {}
        for r in range(len(s)):
            c = s[r]
            freq_s[c] = freq_s.get(c,0)+1

            if c in freq_t:
                if freq_s[c] == freq_t[c]:
                    matching+=1

            while matching == max_matching:
                remove_char = s[l]
                if remove_char in freq_t:
                    freq_s[remove_char]-=1

                    if freq_s[remove_char]+1 == freq_t[remove_char]:
                        found = True
                        matching-=1
                        if r-l+1 < shortest[1]-shortest[0]+1:
                            shortest =(l,r)
                            l+=1
                            break
                l+=1

        return s[shortest[0]:shortest[1]+1] if found else ""