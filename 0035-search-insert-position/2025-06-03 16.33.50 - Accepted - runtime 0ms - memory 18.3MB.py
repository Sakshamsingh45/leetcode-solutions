class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        
        for j in range(len(nums)):
            if nums[j] >= target:
                return j
        
        return len(nums)

