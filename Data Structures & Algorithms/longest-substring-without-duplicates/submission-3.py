class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        longest_substring = 0
        sub = set()
        l = 0

        for i in range(len(s)):
            char = s[i]
            while char in sub:
                sub.remove(s[l])
                l+=1
            sub.add(char)
            longest_substring = max(longest_substring,i-l+1)
        return longest_substring