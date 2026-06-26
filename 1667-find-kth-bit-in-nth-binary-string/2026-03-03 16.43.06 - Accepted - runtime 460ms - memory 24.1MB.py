class Solution:
    def invert(self,st:str):
        rt=""
        for j in st:
            if j=="1":
                rt+="0"
            else:
                rt+="1"
        return rt
    def findKthBit(self, n: int, k: int) -> str:
        s="0"
        for i in range(2,n+1):
            a=self.invert(s)
            s=s+"1"+a[::-1]
        return s[k-1]