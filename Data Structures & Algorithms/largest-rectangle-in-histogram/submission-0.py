class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        max_area = 0
        stack = []

        for i in range(len(heights)):
            curr_height = heights[i]
            start=i

            while stack:
                j,v = stack[-1]
                if v > curr_height:
                    max_area = max((i-j)*v,max_area)
                    stack.pop()
                    start = j
                else:break
            stack.append((start,curr_height))
        max_area = max([max_area]+ list((len(heights)-i[0])*i[1] for i in stack))
        return max_area