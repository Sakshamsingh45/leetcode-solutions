class Solution:
    def maxDifference(self, s: str) -> int:
        a1=[]
        a2=[]
        c=set(s)
        for i in c:
            a=s.count(i)
            if a%2==0:
                a2.append(a)
            else:
                a1.append(a)
        return max(a1)-min(a2)

            
        