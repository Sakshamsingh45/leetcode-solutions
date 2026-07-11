class Solution:
    def minRemoval(self, nums: List[int], k: int) -> int:
        nums.sort()
        l=0
        best=1
        for r in range(len(nums)):
            while nums[r]>nums[l]*k:
                l+=1
            best=max(best,r-l+1)
        return len(nums)-best