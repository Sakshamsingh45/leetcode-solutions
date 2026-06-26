class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxs=float("-inf")
        count=0
        for i in nums:
            count+=i
            if count<i:
                count=i
            if count>maxs:
                maxs=count
        return maxs
