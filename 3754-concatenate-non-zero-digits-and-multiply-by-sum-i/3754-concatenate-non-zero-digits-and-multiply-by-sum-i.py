class Solution:
    def sumAndMultiply(self, n: int) -> int:
        s=0
        newnum=0
        count=0
        while n!=0:
            digit=n%10
            if digit!=0:
                newnum=(digit*(10**count))+newnum
                s+=digit
                count+=1
            n//=10
        return newnum*s
