class Solution:
    def kthCharacter(self, k: int, operations: list[int]) -> str:
        lengths = [1]  # Starting with 'a'

        # 1. Compute lengths of word after each operation
        for op in operations:
            lengths.append(lengths[-1] * 2)
            if lengths[-1] >= k:
                break

        # 2. Walk backward to find the original character
        shift_count = 0
        for i in range(len(lengths) - 1, 0, -1):
            half = lengths[i - 1]
            if k > half:
                k -= half
                if operations[i - 1] == 1:
                    shift_count += 1  # came from shifted part

        # 3. Start from 'a' and apply shift_count shifts
        ch = ord('a')
        ch = (ch - ord('a') + shift_count) % 26 + ord('a')
        return chr(ch)
