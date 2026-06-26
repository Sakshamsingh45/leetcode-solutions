class Solution:
    def maxOperations(self, s: str) -> int:
        s = list(s)
        count = 0
        i = 0

        while i < len(s) - 1:
            if s[i] == "1" and s[i+1] == "0":
                j = i
                # move only through contiguous zeros
                while j + 1 < len(s) and s[j+1] == "0":
                    s[j], s[j+1] = s[j+1], s[j]
                    j += 1
                count += 1
                i = 0
            else:
                i += 1

        return count