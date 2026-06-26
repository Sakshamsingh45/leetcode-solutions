class Solution:
    def reverseWords(self, s: str) -> str:
        a=""
        s=s.strip()
        count=0
        j=len(s)-1
        while j>=0:
            if s[j]!=" ":
                count+=1
            elif count>0:
                a=a+s[j+1:j+1+count]+" "
                count=0
            j-=1
        if count>0:
            a=a+s[j+1:j+1+count]
        return a