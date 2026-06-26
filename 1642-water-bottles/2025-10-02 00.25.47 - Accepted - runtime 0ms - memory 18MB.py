class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        n = numBottles
        m = numExchange
        count = n
        while n // m != 0:
            lb = n % m
            new = n // m
            count += new
            n = new + lb
        return count