class Solution:
    def minOperations(self, nums: list[int], x: int) -> int:
        s=sum(nums)
        if s==x:
            return len(nums)
        elif s<x:
            return -1
        k=s-x
        l=0
        sm=0
        mxlen=0
        for r in range(len(nums)):
            sm+=nums[r]
            while s-sm<x:
                sm-=nums[l]
                l+=1
            if sm==k:
                mxlen=max(mxlen,r-l+1)
        return -1 if mxlen==0 else len(nums)-mxlen