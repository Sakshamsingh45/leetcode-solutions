class Solution:
    def countTriples(self, n: int) -> int:
        count=0
        for i in range(1,n+1):
            for j in range(i+1,n+1):
                sum1= i**2+j**2
                x=int(sum1**0.5)
                if x*x==sum1 and x<=n:
                    count+=2
                else:
                    continue

        return count

            
        