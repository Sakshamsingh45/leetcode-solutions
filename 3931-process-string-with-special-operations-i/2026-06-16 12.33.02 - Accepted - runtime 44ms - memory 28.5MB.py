class Solution:
    def processStr(self, s: str) -> str:
        a=[]
        count=0
        for i in s:
            if i.isalpha():
                a.append(i)
            elif i=="#":
                a=a*2
            elif i=="*" and a:
                a.pop()
            elif i=="%":
                a=a[::-1]
        return "".join(a)