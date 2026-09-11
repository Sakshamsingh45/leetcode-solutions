class Solution:
    def totalNumbers(self, digits: List[int]) -> int:

        s = set()

        for i in range(len(digits)):

            # First digit cannot be 0
            if digits[i] == 0:
                continue

            for j in range(len(digits)):

                for k in range(len(digits)):

                    # Cannot use the same copy of a digit twice
                    if i == j or j == k or i == k:
                        continue

                    # Last digit must be even
                    if digits[k] % 2 != 0:
                        continue

                    num = digits[i] * 100 + digits[j] * 10 + digits[k]

                    s.add(num)

        return len(s)