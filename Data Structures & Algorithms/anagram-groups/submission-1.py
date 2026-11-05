class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        frequencies = {}
        for word in strs:
            word_freq = {}
            for letter in word:
                word_freq[letter] = word_freq.get(letter,0)+1
            word_freq = sorted(word_freq.items())
            word_freq = str(word_freq)

            frequencies[word_freq] = frequencies.get(word_freq,[]) + [word]
        
        res = []
        for freq in frequencies:
            res.append(frequencies[freq])
        return res