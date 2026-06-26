class Solution:
    def totalWaviness(self, num1: int, num2: int) -> int:
        if num2<=100:
            return 0
        ans=0
        for i in range(num1,num2+1):
            s=str(i)
            count=0
            for a,b,c in zip(s,s[1:],s[2:]):
                if a<b>c or a>b<c:
                    count+=1
            ans+=count
        return ans