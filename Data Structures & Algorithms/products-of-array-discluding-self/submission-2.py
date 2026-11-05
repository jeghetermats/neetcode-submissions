class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prod = 1
        res = []
        num_zeros=0
        for num in nums:
            if num==0:
                num_zeros+=1
            if num!=0:
                prod*=num

        for num in nums:
            if num==0:
                if num_zeros>1:
                    res.append(0)
                else: res.append(prod)
            else:
                if num_zeros>0:res.append(0)
                else:
                    res.append(int(prod/num))
        return res