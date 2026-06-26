class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        freq={}
        for i in s:
            freq[i]=freq.get(i,0)+1
        for j in t:
            if freq.get(j,0)==0:
                return j
            freq[j]=freq.get(j)-1