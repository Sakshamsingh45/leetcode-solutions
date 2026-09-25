class Solution:
    def digit_sum(self,n):
        s=0
        while n:
            s+=n%10
            n//=10
        return s
    def smallestIndex(self, nums: List[int]) -> int:
        for i,j in enumerate(nums):
            if self.digit_sum(j)==i:
                return i
        return -1