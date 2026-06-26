class Solution:
    def minimumPrefixLength(self, nums: List[int]) -> int:
        i=len(nums)-1
        while i>0:
            if nums[i-1]>=nums[i]:
                break
            i-=1
        return i
            