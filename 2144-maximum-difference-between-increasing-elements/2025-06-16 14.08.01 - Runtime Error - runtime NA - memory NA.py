class Solution:
    def maximumDifference(self, nums: List[int]) -> int:
        max=-1
        sign=-1
        for i in range (len(nums)):
            for j in range(i+1,len(nums)):
                if nums[i]<nums[j]:a=nums[i]-nums[j]
                if a<0:
                    a=-a
                if a>max and :
                    max=a
        return max
                    
        