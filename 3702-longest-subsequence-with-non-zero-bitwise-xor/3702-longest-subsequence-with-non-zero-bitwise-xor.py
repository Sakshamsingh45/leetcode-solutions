class Solution:
    def longestSubsequence(self, nums: List[int]) -> int:
        totalxor=0
        n=len(nums)
        allzero=True
        for i in nums:
            totalxor^=i
            if i>0:
                allzero=False
        if totalxor>0:
            return n
        return n-1 if allzero==False else 0