class Solution:
    def hammingWeight(self, n: int) -> int:
        a=str(bin(n))
        b=a.count("1")
        return b