class Solution:
    def firstStableIndex(self, nums: list[int], k: int) -> int:
        minarr=[0]*len(nums)
        mn=float("inf")
        for i in range(-1,-len(nums)-1,-1):
            if nums[i]<mn:
                mn=nums[i]
            minarr[i]=mn
        mx=float("-inf")
        for i in range(len(nums)):
            mx=max(mx,nums[i])
            if mx-minarr[i]<=k:
                return i
        return -1