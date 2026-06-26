class Solution:
    def numEquivDominoPairs(self, dominoes: List[List[int]]) -> int:
        count = [0] * 100  # Because 1 <= a, b <= 9 → 10*10 = 100
        result = 0
        for a, b in dominoes:
            key = 10 * min(a, b) + max(a, b)
            result += count[key]
            count[key] += 1
        return result
