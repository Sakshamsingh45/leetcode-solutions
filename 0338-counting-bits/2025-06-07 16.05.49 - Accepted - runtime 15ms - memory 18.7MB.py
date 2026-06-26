class Solution:
    def countBits(self, n: int) -> List[int]:
        a=[]
        for i in range(n+1):
            c=str(bin(i))
            d=a.append(c.count("1"))
        return a