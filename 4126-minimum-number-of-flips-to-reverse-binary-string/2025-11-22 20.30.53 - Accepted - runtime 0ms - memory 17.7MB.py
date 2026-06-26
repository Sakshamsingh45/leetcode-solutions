class Solution:
    def minimumFlips(self, n: int) -> int:
        s=bin(n)[2:]
        count=0
        r=s[::-1]
        for i in range (len(r)):
            if r[i]!=s[i]:
                count+=1
        return count
        