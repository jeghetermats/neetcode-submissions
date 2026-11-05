class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix_prods = []
        postfix_prods = [0]*len(nums)
        prods=[]
        for i in range(len(nums)):
            if i==0:
                prefix_prods.append(1)
            elif i==1:
                prefix_prods.append(nums[0])
            else:
                prefix_prods.append(prefix_prods[i-1] * nums[i-1])

        for i in range(len(nums)-1,-1,-1):
            if i==len(nums)-1:
                postfix_prods[-1]=1
            elif i==len(nums)-2:
                postfix_prods[-2]=(nums[-1])
            else:
                postfix_prods[i]=(postfix_prods[i+1]*nums[i+1])



        for i in range(len(nums)):
            prods.append(prefix_prods[i]*postfix_prods[i])
        return prods