class Solution:
    def isHappy(self, n: int) -> bool:
        while n >9: 
            a = 0
            for i in str(n):
                a += int(i) ** 2
            n = a

        return n == 1
