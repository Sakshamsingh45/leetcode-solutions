class Solution:
    def rotateTheBox(self, boxGrid: List[List[str]]) -> List[List[str]]:
        for k in boxGrid:
            j=i=0
            while i<len(k) and j<len(k):
                if k[j]=="*":
                    i=j
                    i+=1
                    j+=1
                    continue
                if k[j]=="#":
                    j+=1
                    continue
                if k[j]==k[i]:
                    j+=1
                    i+=1
                    continue
                if k[j]=="." and k[i]=="#":
                    k[j],k[i]="#","."
                    i+=1
                    j+=1
        return [list(a) for a in zip(*boxGrid[::-1])]
                