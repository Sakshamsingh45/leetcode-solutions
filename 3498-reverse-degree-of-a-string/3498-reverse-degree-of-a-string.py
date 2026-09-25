class Solution:
    def reverseDegree(self, s: str) -> int:
        res=0
        for i,j in enumerate(s):
            mul=27-(ord(j)-96)
            res+=(i+1)*mul
        return res