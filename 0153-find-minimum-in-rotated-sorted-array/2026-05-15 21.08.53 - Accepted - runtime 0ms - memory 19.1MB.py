class Solution:
    def findMin(self, nums: List[int]) -> int:
        i=0
        n=len(nums)
        while i<n//2:
            j=n-i-1
            if nums[i+1]<nums[i]:
                return nums[i+1]
            if nums[j-1]>nums[j]:
                return nums[j]
            i+=1
            j-=1
        return min(nums[0],nums[-1])