class Solution:
    def maxSum(self, nums: List[int]) -> int:
        count=0
        nums=set(nums)
        for i in nums:
            if i>0:
                count+=i
        return count