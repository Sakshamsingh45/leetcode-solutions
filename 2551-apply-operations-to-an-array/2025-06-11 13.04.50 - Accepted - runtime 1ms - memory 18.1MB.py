class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:
        i = 0
        while i < len(nums) - 1:
            if nums[i] == nums[i + 1] and nums[i] != 0:
                nums[i] *= 2
                nums[i + 1] = 0
                i += 1
            i += 1

        pos = 0
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[pos] = nums[i]
                pos += 1

        while pos < len(nums):
            nums[pos] = 0
            pos += 1

        return nums
