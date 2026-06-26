class Solution:
    def addBinary(self, a: str, b: str) -> str:
        carry=0
        i=-1
        ans=""
        while -len(a)<=i or -len(b)<=i:
            s=carry
            if -len(a)<=i:
                s+=int(a[i])
            if -len(b)<=i:
                s+=int(b[i])
            if s>1:
                carry=1
            else:
                carry=0
            s=s%2
            ans=str(s)+ans
            i=i-1
        if carry:
            ans="1"+ans
        return ans