class Solution:
    def minPairSum(self, nums: List[int]) -> int:
        nums.sort()
        i,j=0,len(nums)-1
        s=0
        while i<j:
            temp=nums[i]+nums[j]
            if temp>s:
                s=temp
            i+=1
            j-=1
        return s