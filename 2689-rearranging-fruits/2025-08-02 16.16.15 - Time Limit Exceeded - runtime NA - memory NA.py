class Solution:
    def minCost(self, basket1: List[int], basket2: List[int]) -> int:
        freq = {}
        all_items = basket1 + basket2
        for x in all_items:
            freq[x] = freq.get(x, 0) + 1

        # If any item occurs odd number of times, not possible
        for val in freq.values():
            if val % 2 != 0:
                return -1

        # Build surplus elements
        surplus1 = []
        surplus2 = []
        for x in set(all_items):
            c1 = basket1.count(x)
            c2 = basket2.count(x)
            diff = (c1 - c2) // 2
            if diff > 0:
                surplus1 += [x] * diff
            elif diff < 0:
                surplus2 += [x] * (-diff)

        surplus1.sort()
        surplus2.sort(reverse=True)

        min_val = min(all_items)
        cost = 0
        for x, y in zip(surplus1, surplus2):
            cost += min(2 * min_val, min(x, y))
        return cost
