class Solution:
    def canAliceWin(self, n: int) -> bool:
        if n<10:
            return False
        flag=True
        n-=10
        i=9
        while n>=i:
            n-=i
            flag=not flag
            i-=1
        return flag