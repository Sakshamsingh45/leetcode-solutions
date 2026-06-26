class Solution:
    def mergeAdjacent(self, nums: List[int]) -> List[int]:
        i=0
        while i<len(nums)-1:
            if nums[i]==nums[i+1]:
                nums[i]=nums[i]+nums[i+1]
                nums.pop(i+1)
                if i>0:
                    i-=1
            else:
                i+=1
                
        return nums