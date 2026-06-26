class Solution:
    def maxAdjacentDistance(self, nums: List[int]) -> int:
        max_diff = 0
        n = len(nums)
        for i in range(n):
            next_index = (i + 1) % n
            diff = nums[next_index] - nums[i]
            if diff < 0:
                diff = -diff
            if diff > max_diff:
                max_diff = diff
        return max_diff
