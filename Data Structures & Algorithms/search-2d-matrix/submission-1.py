class Solution:
    def binary_search(self, nums,target):
        l,r = 0, len(nums)-1
        while l<=r:
            mid = l + (r-l)//2
            if nums[mid] == target:return mid

            if nums[mid]<target:
                l=mid+1
            else:
                r=mid-1
        return l,r
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows = [i[0] for i in matrix]
        row = self.binary_search(rows,target)
        if type(row)==int: return True
        row = matrix[row[1]]
        if type(self.binary_search(row,target)) == int:return True
        return False