class Solution:
    def minCost(self, basket1: List[int], basket2: List[int]) -> int:
        freq = {}
        freq1 = {}
        freq2 = {}

        # Build frequency maps
        for x in basket1:
            freq[x] = freq.get(x, 0) + 1
            freq1[x] = freq1.get(x, 0) + 1
        for x in basket2:
            freq[x] = freq.get(x, 0) + 1
            freq2[x] = freq2.get(x, 0) + 1

        # If any item appears an odd number of times, return -1
        for v in freq.values():
            if v % 2 != 0:
                return -1

        # Find the surplus elements that need to be swapped
        surplus1 = []
        surplus2 = []

        for x in freq:
            c1 = freq1.get(x, 0)
            c2 = freq2.get(x, 0)
            diff = (c1 - c2) // 2
            if diff > 0:
                surplus1.extend([x] * diff)
            elif diff < 0:
                surplus2.extend([x] * (-diff))

        surplus1.sort()
        surplus2.sort(reverse=True)

        min_val = min(freq.keys())
        cost = 0
        for x, y in zip(surplus1, surplus2):
            cost += min(2 * min_val, min(x, y))

        return cost
