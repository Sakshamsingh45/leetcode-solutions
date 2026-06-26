class Solution:
    def minimumDeletions(self, word: str, k: int) -> int:
        freq = [0] * 26
        for c in word:
            freq[ord(c) - ord('a')] += 1

        # Remove zeros for efficiency
        freq = [f for f in freq if f > 0]

        min_deletions = float('inf')

        # Try every possible target frequency
        for target in range(1, max(freq) + 1):
            deletions = 0
            for f in freq:
                if f > target + k:
                    deletions += f - (target + k)
                elif f < target:
                    deletions += f
            if deletions < min_deletions:
                min_deletions = deletions

        return min_deletions
