class Solution:
    def numSteps(self, s: str) -> int:
        count=0
        while s!="1":
            if s[-1]=="0":
                s=s[:len(s)-1]
            else:
                d=int(s,2)
                d+=1
                s=bin(d)[2:]
            count+=1
        return count