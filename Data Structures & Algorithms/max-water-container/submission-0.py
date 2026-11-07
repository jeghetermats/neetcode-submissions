class Solution:
    def maxArea(self, heights: List[int]) -> int:
        maxA = 0

        l,r = 0, len(heights)-1

        while l<r:
            currA = min(heights[l], heights[r])*(r-l)
            if currA > maxA:
                maxA = currA
                print(l,r)
            if heights[l]<heights[r]:
                l+=1
            else:r-=1
        return maxA