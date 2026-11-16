class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        from math import ceil
        min_k = 1
        max_k = max(piles)

        while min_k<=max_k:
            k = (max_k+min_k)//2
            curr_h = sum([ceil(i/k) for i in piles])
            if curr_h <= h:
                max_k = k-1 
            else:
                min_k = k+1
            
        return min_k