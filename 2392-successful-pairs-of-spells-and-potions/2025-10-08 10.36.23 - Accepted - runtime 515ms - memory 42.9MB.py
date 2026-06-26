class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        potions.sort()
        n = len(potions)
        pairs = []

        for s in spells:
            # Minimum potion value required
            threshold = (success + s - 1) // s  # same as ceil(success / s)

            # --- Manual binary search ---
            left, right = 0, n - 1
            while left <= right:
                mid = (left + right) // 2
                if potions[mid] < threshold:
                    left = mid + 1
                else:
                    right = mid - 1

            # After the loop, 'left' is the first index where potions[left] >= threshold
            pairs.append(n - left)

        return pairs
