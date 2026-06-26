class Solution:
    def minimumPairRemoval(self, nums: List[int]) -> int:
        count=0
        i=0
        minsum=float("inf")
        j,k=0,0
        while True:
            if i+1>=len(nums) and minsum==float('inf') :
                break
            if i+1>=len(nums):
                nums[j]=minsum
                nums.pop(k)
                minsum=float('inf')
                j,k,i=0,0,0
                count+=1
            if nums[i]>=nums[i+1]:
                
            else:
                tempsum=nums[i]+nums[i+1]
            if tempsum < minsum:
                minsum=tempsum
                j,k=i,i+1
            i+=1
        return count
            
            
        