class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        longest_sub = 0
        alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        for char in alphabet:
            replacements=k
            l,r = 0,0
            while r < len(s):
                if s[r] != char:
                    while replacements == 0:
                        if l > len(s)-1:
                            break
                        if s[l] != char:
                            replacements+=1
                    
                        l+=1
                    replacements-=1
                longest_sub = max(longest_sub,r-l+1)
                r+=1
        return longest_sub