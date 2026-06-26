class Solution:
    def kthCharacter(self, k: int, operations: list[int]) -> str:
        length = 1  # Start with length of "a"
        ops_len = []

        # Step 1: Forward pass — compute total length after each operation
        for op in operations:
            if op == 0:
                length *= 2
            else:
                length *= 2
            ops_len.append(length)
            if length >= k:
                break

        # Step 2: Reverse simulation
        for i in range(len(ops_len) - 1, -1, -1):
            length //= 2
            op = operations[i]

            if k > length:
                k -= length
                if op == 1:
                    # This char was from shifted half → we shift it back later
                    shift = True
                else:
                    shift = False
            else:
                shift = False

        # Final character is 'a', possibly shifted forward
        ch = ord('a')
        if shift:
            ch = (ch + 1 - ord('a')) % 26 + ord('a')

        return chr(ch)
