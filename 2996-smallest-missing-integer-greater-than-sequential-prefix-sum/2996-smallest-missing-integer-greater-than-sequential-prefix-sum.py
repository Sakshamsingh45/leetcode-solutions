class Solution:
    def missingInteger(self, nums: List[int]) -> int:
        num_set=set(nums)
        sm=0
        for i in range(len(nums)):
            if i==0 or nums[i-1]+1==nums[i]:
                sm+=nums[i]
            else:
                break
        while sm in num_set:
            sm+=1
        return sm