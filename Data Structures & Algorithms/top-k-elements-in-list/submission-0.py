class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        frequency = {}
        for num in nums:
            frequency[num] = frequency.get(num,0)+1

        frequency = sorted(frequency.items(),key = lambda item: item[1],reverse=True)
        frequency = [i[0] for i in frequency]
        return frequency[:k]