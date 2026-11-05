class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        frequencies = {}
        for word in strs:
            sorted_word = "".join(sorted(word))



            frequencies[sorted_word] = frequencies.get(sorted_word,[]) + [word]
        
        return list(frequencies.values())