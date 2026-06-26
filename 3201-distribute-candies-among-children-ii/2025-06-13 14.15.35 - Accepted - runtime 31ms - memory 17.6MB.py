class Solution:
    def distributeCandies(self, n: int, limit: int) -> int:
        def nCr(n, r):
            if r < 0 or n < r:
                return 0
            result = 1
            for i in range(1, r + 1):
                result = result * (n - i + 1) // i
            return result

        def count_ways(total):
            if total < 0:
                return 0
            return nCr(total + 2, 2)

        total = count_ways(n)
        total -= 3 * count_ways(n - (limit + 1))
        total += 3 * count_ways(n - 2 * (limit + 1))
        total -= count_ways(n - 3 * (limit + 1))
        
        return total
