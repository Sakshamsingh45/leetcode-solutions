class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:
        max0=nums[0]
        for i in range (1,len(nums)):
            if nums[i]>nums[i-1]:
                max0+=nums[i]
            else:
                max0=nums[i]
        return max0