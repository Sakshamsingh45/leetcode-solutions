class Solution:
    def maxProfit(self, prices: List[int], strategy: List[int], k: int) -> int:
        n = len(prices)
        half = k // 2

        freq = {0: 0}
        for i in range(n):
            freq[i + 1] = freq[i] + prices[i] * strategy[i]

        base = freq[n]
        res = base   # ⭐ important fix

        rightsum = 0

        # initial window
        for m in range(k):
            if m >= half:
                rightsum += prices[m]

        res = max(res, base - (freq[k] - freq[0]) + rightsum)

        # slide window
        for j in range(1, n):
            if j + k - 1 >= n:
                break

            rightsum -= prices[j - 1 + half]
            rightsum += prices[j + k - 1]

            res = max(
                res,
                base - (freq[j + k] - freq[j]) + rightsum
            )

        return res