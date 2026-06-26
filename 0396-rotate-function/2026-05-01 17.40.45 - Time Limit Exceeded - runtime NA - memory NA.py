class Solution:
    def maxRotateFunction(self, nums: List[int]) -> int:
        ans=[0]*len(nums)
        ma=float("-inf")
        count=0
        while count<len(nums):
            temp=0
            to=0
            for i in range(count,count+len(nums)):
                to+=temp*nums[i%len(nums)]
                temp+=1
            count+=1
            if ma<to:
                ma=to
        return ma