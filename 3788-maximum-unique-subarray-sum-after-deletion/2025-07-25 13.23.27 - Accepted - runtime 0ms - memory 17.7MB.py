class Solution:
    def maxSum(self, nums: List[int]) -> int:
        count=0
        neg=max(nums)
        nums=set([num for num in nums if num>0])
        if neg<0:
            return neg
        else:
            return sum(nums)