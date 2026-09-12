class Solution:
    def integerReplacement(self, n: int) -> int:
        count=0
        while n!=1:
            if n%2==0:
                n=n//2
            else:
                if n==3 or not((n>>1)&1):
                    n-=1
                else:
                    n+=1
            count+=1
        return count