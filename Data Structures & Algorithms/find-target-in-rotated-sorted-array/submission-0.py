class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums)-1
        midpoint=0
        #leter etter minimum for å finne splitten
        while l<r:
            mid = l + (r-l)//2
            mid_point = nums[mid]
            right_point = nums[r]
            if mid_point > right_point:
                #splittet ligger mellom mid og right
                l = mid+1
            else:
                r = mid
        split = l
        

        l, r = 0, len(nums)-1

        while l<=r:
            mid  = l + (r-l)//2
            real = (mid + split) % len(nums)
            if nums[real] == target:
                return real
            if nums[real] < target:
                l = mid+1
            else:
                r = mid-1
        return -1