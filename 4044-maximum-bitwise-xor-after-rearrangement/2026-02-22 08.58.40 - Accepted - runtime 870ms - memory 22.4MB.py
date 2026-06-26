class Solution:
    def maximumXor(self, s: str, t: str) -> str:
        freq={}
        newstr=""
        for i in t:
            freq[i]=freq.get(i,0)+1
        for i in s:
            if i =="0":
                if freq.get("1",0)>0:
                    newstr+="1"
                    freq["1"]-=1
                else:
                    newstr+="0"
                    freq["0"]-=1
            else:
                if freq.get("0",0)>0:
                    newstr+="1"
                    freq["0"]-=1
                else:
                    newstr+="0"
                    freq["1"]-=1
        return newstr
                