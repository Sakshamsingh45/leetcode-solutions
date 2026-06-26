class Solution:
    def countHillValley(self, nums: List[int]) -> int:
        count = 0
        n = len(nums)

        for i in range(1, n - 1):
            # Skip if nums[i] is same as previous (handled in prior iteration)
            if nums[i] == nums[i - 1]:
                continue

            # Find the closest different number to the left
            left = i - 1
            while left >= 0 and nums[left] == nums[i]:
                left -= 1

            # Find the closest different number to the right
            right = i + 1
            while right < n and nums[right] == nums[i]:
                right += 1

            # Make sure we are within bounds
            if left >= 0 and right < n:
                if nums[i] > nums[left] and nums[i] > nums[right]:
                    count += 1  # Hill
                elif nums[i] < nums[left] and nums[i] < nums[right]:
                    count += 1  # Valley

        return count
