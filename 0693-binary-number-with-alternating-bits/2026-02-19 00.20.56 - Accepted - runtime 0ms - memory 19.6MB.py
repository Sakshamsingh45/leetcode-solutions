class Solution:
    def hasAlternatingBits(self, n: int) -> bool:
        n=bin(n)[2:]
        b="-1"
        for i in n:
            if i==b:
                return False
            b=i
        return True

