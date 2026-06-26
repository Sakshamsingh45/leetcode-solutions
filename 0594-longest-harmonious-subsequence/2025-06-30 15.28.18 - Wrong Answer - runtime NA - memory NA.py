class Solution:
    def findLHS(self, nums: List[int]) -> int:
        ans=set(nums)
        max=0
        for i in range(len(ans)):
            for j in range(i+1,len(ans)):
                if abs(nums[i]-nums[j])==1:
                    if max<nums.count(nums[i])+nums.count(nums[j]):
                        max=nums.count(nums[i])+nums.count(nums[j])
        return max