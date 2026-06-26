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
        while i<len(s) and s[i].isdigit():
            a=a+s[i]
            i+=1
        if not a:
            return 0
        return int(a)*sign

        
        