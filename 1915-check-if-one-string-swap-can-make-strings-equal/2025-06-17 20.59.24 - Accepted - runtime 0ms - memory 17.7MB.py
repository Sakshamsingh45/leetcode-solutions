class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        i=0
        if len(s1) != len(s2):
            return False
        s1=list(s1)
        s2=list(s2)
        left,right=0,len(s1)-1
        while left<right:
            if s1[left]==s2[left] and s1[right]==s2[right]:
                left+=1
                right-=1
            elif s1[left]!=s2[left] and s1[right]!=s2[right]:
                s2[left],s2[right]=s2[right],s2[left]
                left=len(s1)
                
            elif s1[left]!=s2[left]:
                right-=1
            elif s1[right]!=s2[right]:
                left+=1
            
        return s1==s2

