class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        sm=sum(nums[:k])
        msm=sm
        for i in range(k,len(nums)):
            sm=sm-nums[i-k]+nums[i]
            msm=max(sm,msm)
        return msm/k