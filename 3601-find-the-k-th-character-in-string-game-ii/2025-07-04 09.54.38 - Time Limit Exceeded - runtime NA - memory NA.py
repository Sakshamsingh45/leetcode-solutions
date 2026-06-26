class Solution:
    def kthCharacter(self, k: int, operations: list[int]) -> str:
        word = ["a"]

        for op in operations:
            if op == 0:
                word += word[:]  # append a copy of current word
            else:  # op == 1
                shifted = []
                for ch in word:
                    next_char = chr((ord(ch) - ord('a') + 1) % 26 + ord('a'))
                    shifted.append(next_char)
                word += shifted  # append shifted version

            # Optimization: Stop if word already has enough characters
            if len(word) >= k:
                break

        return word[k - 1]  # 1-based indexing → 0-based
