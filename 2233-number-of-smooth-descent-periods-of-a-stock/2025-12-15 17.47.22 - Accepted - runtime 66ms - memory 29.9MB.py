class Solution:
    def getDescentPeriods(self, prices: List[int]) -> int:
        count = 0
        length = 0
        for i in range(len(prices)):
            if i > 0 and prices[i - 1] - 1 == prices[i]:
                length += 1
            else:
                length = 1
            count += length
        return count