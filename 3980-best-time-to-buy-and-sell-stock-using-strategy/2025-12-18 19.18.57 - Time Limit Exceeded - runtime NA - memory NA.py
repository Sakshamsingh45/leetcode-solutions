class Solution:
    def maxProfit(self, prices: List[int], strategy: List[int], k: int) -> int:
        n = len(prices)
        p = [0] * (n + 1)
        for i in range(n):
            p[i + 1] = p[i] + prices[i] * strategy[i]
        base_profit = p[n]
        max_extra = 0
        a = 0
        while a + k <= n:
            extra = 0
            for i in range(a, a + k // 2):
                extra -= prices[i] * strategy[i]
            for i in range(a + k // 2, a + k):
                extra += prices[i] * (1 - strategy[i])
            max_extra = max(max_extra, extra)
            a += 1

        return base_profit + max_extra