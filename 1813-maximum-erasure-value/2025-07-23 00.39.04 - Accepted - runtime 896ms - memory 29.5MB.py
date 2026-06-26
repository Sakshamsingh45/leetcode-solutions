class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        current_sum = 0
        max_sum = 0
        a = []

        for i in nums:
            if i not in a:
                a.append(i)
                current_sum += i
            else:
                index = a.index(i)
                # Remove elements before and including duplicate
                for _ in range(index + 1):
                    removed = a.pop(0)
                    current_sum -= removed
                # Now add the current element
                a.append(i)
                current_sum += i

            max_sum = max(max_sum, current_sum)

        return max_sum
