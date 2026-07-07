class Solution:
    def sumAndMultiply(self, n: int) -> int:
        if n==0:
            return 0
        n=str(n)
        newnum=""
        s=0
        for i in n:
            if i!="0":
                newnum=newnum+i
                s+=int(i)
        return int(newnum)*s
