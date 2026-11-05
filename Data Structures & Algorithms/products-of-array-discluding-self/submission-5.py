class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        pre = [0]*len(nums)
        post  =[0]*len(nums)
        for i in range(len(nums)):
            if i == 0:
                pre[i]=nums[0]
            else:
                pre[i] = pre[i-1] * nums[i]
        
        for i in range(len(nums)-1,-1,-1):
            if i==len(nums)-1:
                post[i]=nums[i]
            else:
                post[i]=post[i+1]*nums[i]

        res =[]
        for i in range(len(nums)): 
            if i ==0:
                res.append(post[1])
            elif i==len(nums)-1:
                res.append(pre[-2])
            else:
                res.append(pre[i-1]*post[i+1])
        return res