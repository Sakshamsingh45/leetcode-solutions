class Solution:
    def hasAlternatingBits(self, n: int) -> bool:
        n=bin(n)[2:]
        b=1
        for i in n:
            i=int(i)
            if i==b and b==0:
                b=1
            elif i==b and b==1:
                b=0
            else:
                return False
        return True

