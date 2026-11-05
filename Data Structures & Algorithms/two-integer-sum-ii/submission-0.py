class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        d = {}
        for i in range(len(numbers)):
            number = numbers[i]
            if target - number in d:
                return [d[target-number],i+1]
            d[number]=i+1
            