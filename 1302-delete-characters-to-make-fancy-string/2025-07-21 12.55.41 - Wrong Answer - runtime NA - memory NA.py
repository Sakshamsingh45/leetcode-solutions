class Solution:
    def makeFancyString(self, s: str) -> str:
        ans=""+s[0]
        count=0
        for i in range(1,len(s)):
            pev=s[i-1]
            if s[i]==pev:
                count+=1

            elif count>=2:
                count=0

            if count<2:
                ans+=s[i]
        return ans