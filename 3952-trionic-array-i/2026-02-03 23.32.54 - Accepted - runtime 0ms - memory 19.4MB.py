class Solution:
    def isTrionic(self, nums: List[int]) -> bool:
        i=1
        while i<len(nums) and nums[i-1]<nums[i]:
            i+=1
        p=i-1
        while i<len(nums) and nums[i-1]>nums[i]:
            i+=1
        q=i-1
        while i<len(nums) and nums[i-1]<nums[i]:
            i+=1
        k=i-1
        return p!=q and p!=0 and i==len(nums) and k!=q