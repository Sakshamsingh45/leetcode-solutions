class Solution:
    def getSumAbsoluteDifferences(self, nums: List[int]) -> List[int]:
        sum_before,sum_after=0,sum(nums)
        res=[0]*len(nums)
        for i in range(len(nums)):
            sum_after-=nums[i]
            res[i]=abs((sum_after-(nums[i]*(len(nums)-(i+1)))))+abs((sum_before-(nums[i]*i)))
            sum_before+=nums[i]
        return res