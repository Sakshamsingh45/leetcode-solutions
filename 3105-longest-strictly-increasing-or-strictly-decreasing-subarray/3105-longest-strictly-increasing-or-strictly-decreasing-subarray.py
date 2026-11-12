class Solution:
    def longestMonotonicSubarray(self, nums: List[int]) -> int:
        n=len(nums)
        if n==1:
            return nums[0]
        i=1
        mx_len=1
        while i<len(nums):
            temp=0
            while i<len(nums) and nums[i-1]<nums[i]:
                temp+=1
                i+=1
                mx_len=max(mx_len,temp+1)
            temp=0
            while i<len(nums) and nums[i-1]>nums[i]:
                temp+=1
                i+=1
                mx_len=max(mx_len,temp+1)
            while i<len(nums) and nums[i-1]==nums[i]:
                i+=1
        return mx_len