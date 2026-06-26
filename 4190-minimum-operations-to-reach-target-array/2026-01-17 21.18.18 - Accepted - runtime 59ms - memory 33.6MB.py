class Solution:
    def minOperations(self, nums: List[int], target: List[int]) -> int:
        bad=set()
        for i in range(len(nums)):
            if nums[i]!=target[i]:
                bad.add(nums[i])
        return len(bad)