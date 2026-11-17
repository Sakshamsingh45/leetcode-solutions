class Solution:
    def digitSum(self, s: str, k: int) -> str:
        if len(s)<=k:
            return s
        while len(s)>k:
            temp=""
            count=0
            for i in range(len(s)):
                count+=int(s[i])
                if (i+1)%k==0 or i==len(s)-1:
                    temp+=str(count)
                    count=0
            s=temp
        return s