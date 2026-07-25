class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        l=0
        count=len(nums)+1
        sm=0
        for r in range(len(nums)):
            sm+=nums[r]
            while sm>=target:
                count=min(count,r-l+1)
                sm-=nums[l]
                l+=1
        return 0 if count==len(nums)+1 else count
