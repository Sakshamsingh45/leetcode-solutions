class Solution:
    def bitwiseComplement(self, n: int) -> int:
        n=bin(n)[2:]
        s="".join("1" if i=="0" else "0" for i in n)
        return int(s,2)