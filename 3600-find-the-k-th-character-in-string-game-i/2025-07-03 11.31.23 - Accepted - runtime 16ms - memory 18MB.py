class Solution:
    def kthCharacter(self, k: int) -> str:
        word = ["a"]

        while len(word) < k:
            # Generate next part by shifting each char in word
            next_part = []
            for c in word:
                # Shift with wrap-around ('z' to 'a')
                shifted = chr((ord(c) - ord('a') + 1) % 26 + ord('a'))
                next_part.append(shifted)

            word += next_part  # Append the transformed part

        return word[k - 1]
