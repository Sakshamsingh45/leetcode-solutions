class Solution:
    def minimumDeletions(self, nums: List[int]) -> int:
        n=len(nums)
        if n==1:
            return 1
        elif n==2:
            return 2
        mn,mx=float("inf"),float("-inf")
        mnidx,mxidx=0,0
        for i,j in enumerate(nums):
            if j>mx:
                mx=j
                mxidx=i
            if j<mn:
                mn=j
                mnidx=i
        left=min(mnidx,mxidx)
        right=max(mnidx,mxidx)
        dis=min(right,n-left-1)
        dis2=left+(n-1-right)
        if dis<=dis2:
            return dis+1
        else:
            return dis2+2
        