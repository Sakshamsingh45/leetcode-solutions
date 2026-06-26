class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:
        i=0
        count=0
        while i < len(nums)-1:
            if nums[i]==0:
                nums.pop(i)
                nums.append(0)
            if nums[i]==nums[i+1]:
                nums[i]=nums[i]*2
                nums[i+1]=0
            i+=1

        return nums
