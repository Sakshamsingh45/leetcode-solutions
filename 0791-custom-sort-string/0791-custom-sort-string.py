class Solution:
    def customSortString(self, order: str, s: str) -> str:
        freq={}
        for i in s:
            freq[i]=freq.get(i,0)+1
        res=""
        for j in order:
            if j in freq:
                res+=j*freq[j]
                del freq[j]
        for k in freq:
            res+=k*freq[k]
        return res