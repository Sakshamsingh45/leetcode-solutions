class Solution:
    def distributeCandies(self, n: int, limit: int) -> int:
        count = 0
        for i in range(0, min(n, limit) + 1):
            for j in range(0, min(n - i, limit) + 1):
                k = n - i - j
                if 0 <= k <= limit:
                    count += 1
        return count
