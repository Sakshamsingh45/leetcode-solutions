class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        seen=set()
        sm=0
        msm=0
        l=0
        for r in range(len(nums)):
            if nums[r] in seen:
                while nums[r] in seen:
                    seen.remove(nums[l])
                    sm-=nums[l]
                    l+=1
            seen.add(nums[r])
            sm+=nums[r]
            msm=max(sm,msm)
        return msm
