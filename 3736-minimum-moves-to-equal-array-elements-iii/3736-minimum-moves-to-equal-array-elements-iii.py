class Solution:
    def minMoves(self, nums: List[int]) -> int:
        mx=max(nums)
        count=0
        for i in nums:
            if i<mx:
                count+=mx-i
        return count
