class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        l=0
        sm=sum(nums[:k])
        ag=sm/k
        r=k
        while r<len(nums):
            sm=sm-nums[l]+nums[r]
            ag=max(ag,sm/k)
            l+=1
            r+=1
        return ag