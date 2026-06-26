class Solution:
    def reverseByType(self, s: str) -> str:
        sp=[]
        le=[]
        ans=[]
        for i in s:
            if i.isalpha():
                le.append(i)
            else:
                sp.append(i)
        sp.reverse()
        le.reverse()
        li=si=0
        for i in s:
            if i.isalpha():
                ans.append(le[li])
                li+=1
            else:
                ans.append(sp[si])
                si+=1
        return "".join(ans)