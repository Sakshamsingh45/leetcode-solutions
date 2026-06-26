
class Solution:
    def findKDistantIndices(self, nums: List[int], key: int, k: int) -> List[int]:
        sol = set()  # Use a set to avoid duplicates

        for i in range(len(nums)):
            if nums[i] == key:
                # Add all indices j such that abs(i - j) <= k
                for j in range(max(0, i - k), min(len(nums), i + k + 1)):
                    sol.add(j)

        return sorted(sol)
