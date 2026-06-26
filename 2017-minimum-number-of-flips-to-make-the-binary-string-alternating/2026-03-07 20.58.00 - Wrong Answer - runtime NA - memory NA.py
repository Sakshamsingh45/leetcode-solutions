class Solution:
    def minFlips(self, s: str) -> int:
        if "00" not in s and "11" not in s:
            return 0
        s=list(s)
        while s[-1]!=s[0] :
            a=s[0]
            s.pop(0)
            s.append(a)
        s0,s1=0,0
        for i in range(len(s)):
            if i%2==0:
                if s[i]=="1":
                    s1+=1
                else:
                    s0+=1
            else:
                if s[i]=="0":
                    s1+=1
                else:
                    s0+=1
        return min(s0,s1)