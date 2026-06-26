class Solution:
    def maximumLength(self, nums: List[int]) -> int:
        n = len(nums)
        max_len = 1

        # Try for both parities: 0 and 1
        for parity in [0, 1]:
            length = 1
            prev = nums[0]
            for i in range(1, n):
                if (prev + nums[i]) % 2 == parity:
                    length += 1
                    prev = nums[i]
                # if not matching, skip nums[i] (don't update prev)
            if length > max_len:
                max_len = length

        return max_len
