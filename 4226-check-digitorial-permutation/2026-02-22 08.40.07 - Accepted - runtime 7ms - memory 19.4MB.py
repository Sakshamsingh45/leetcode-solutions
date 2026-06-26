class Solution:
    def isDigitorialPermutation(self, n: int) -> bool:
        temp=n
        factsum=0
        while n>0:
            f=n%10
            fact=1
            for i in range(1,f+1):
                fact*=i
            factsum+=fact
            n=n//10
        temp=sorted(str(temp))
        factsum=sorted(str(factsum))
        if temp!=factsum:
            return False
        return True
            