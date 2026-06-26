class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        a=0
        for i in range(0,len(nums)):
            if(a==1):
                break
            for j in range(i+1,len(nums)):
                if((nums[i]+nums[j])==target):
                    self=[i,j]
                    a=1
                    return self
                    


        