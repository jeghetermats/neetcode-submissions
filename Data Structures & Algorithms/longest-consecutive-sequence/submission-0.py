class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        s = set(nums)
        starters=[]
        for num in nums:
            if not num-1 in s:
                starters.append(num)
        
        longest = 0
        for starter in starters:
            next = starter+1
            while next in s:
                next+=1
            longest = max(longest,next-starter)
        return longest