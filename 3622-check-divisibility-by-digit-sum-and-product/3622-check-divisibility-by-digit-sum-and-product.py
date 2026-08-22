class Solution:
    def checkDivisibility(self, n: int) -> bool:
        temp=n
        sm=0
        pr=1
        while temp:
            digit=temp%10
            sm+=digit
            pr*=digit
            temp//=10
        return n%(sm+pr)==0