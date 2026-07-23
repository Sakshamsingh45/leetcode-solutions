class Solution:
    def uniqueXorTriplets(self, nums: List[int]) -> int:
        if len(nums)<=2:
            return len(nums)
        ans=1
        while ans<=len(nums):
            ans<<=1
        return ans