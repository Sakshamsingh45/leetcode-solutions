class Solution:
    def maxSubsequence(self, nums: List[int], k: int) -> List[int]:
        while len(nums)>k:
            a=min(nums)
            nums.remove(a)

        return nums