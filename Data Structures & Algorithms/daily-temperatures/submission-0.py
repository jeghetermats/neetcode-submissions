class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        result = [0]* len(temperatures)
        stack = []
        indexes = []

        for i in range(len(temperatures)):
            curr = temperatures[i]
            
            while stack and curr > stack[-1]:
                result[indexes[-1]] = i - indexes[-1]
                stack.pop()
                indexes.pop()
            
            stack.append(curr)
            indexes.append(i)
        return result