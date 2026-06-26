class Solution:
    def myAtoi(self, s: str) -> int:
        s=s.strip()
        if not s:
            return 0
        a=""
        i=0
        sign=1
        if s[0]=="-":
            i=i+1
            sign=-1
        elif s[0]=="+":
            i=i+1
        while i<len(s) and s[i].isdigit():
            a=a+s[i]
            i+=1
        if not a:
            return 0
        a=int(a)*sign
        if a< -(2**31):
            return -(2**31)
        elif a>(2**31)-1:
            return (2**31)-1
        return a

        
        