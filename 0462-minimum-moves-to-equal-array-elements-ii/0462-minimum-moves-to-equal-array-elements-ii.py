class Solution:
    def minMoves2(self, nums: list[int]) -> int:
        nums.sort()
        if nums[0]==nums[-1]:
            return 0
        median=(nums[len(nums)//2]+nums[(len(nums)+1)//2])//2 if len(nums)%2==0 else nums[len(nums)//2]
        count=0
        for i in nums:
            if i <median:
                count+=median-i
            else:
                count+=i-median
        return count