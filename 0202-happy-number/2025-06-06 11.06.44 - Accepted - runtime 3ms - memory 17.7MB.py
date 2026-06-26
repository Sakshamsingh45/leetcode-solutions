class Solution:
    def isHappy(self, n: int) -> bool:
        while n != 1 and n != 4: 
            a = 0
            for i in str(n):
                a += int(i) ** 2
            n = a

        return n == 1
