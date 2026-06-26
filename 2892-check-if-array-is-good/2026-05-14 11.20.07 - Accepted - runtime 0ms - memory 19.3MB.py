class Solution:
    def isGood(self, nums: List[int]) -> bool:
        nums.sort()
        if len(nums)!=nums[-1]+1:
            return False
        for i in range(1,nums[-1]+1):
            if nums[i-1]!=i:
                return False
        if nums[-1]!=len(nums)-1:
            return False
        return True