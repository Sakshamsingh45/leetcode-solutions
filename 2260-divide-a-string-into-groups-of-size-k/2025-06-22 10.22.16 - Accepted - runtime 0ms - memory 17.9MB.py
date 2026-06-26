class Solution:
    def divideString(self, s: str, k: int, fill: str) -> List[str]:
        a=len(s)
        b=[]
        if a%k!=0:
            s=s+(fill*(k-a%k))
        i =0
        while i <len(s):
            b.append(s[i:i+k])
            i=i+k
        return b
