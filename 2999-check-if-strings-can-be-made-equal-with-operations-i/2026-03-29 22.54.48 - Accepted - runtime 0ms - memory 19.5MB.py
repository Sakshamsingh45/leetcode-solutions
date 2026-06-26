class Solution:
    def canBeEqual(self, s1: str, s2: str) -> bool:
        s1,s2=list(s1),list(s2)
        for i in range(len(s1)-2):
            if s1[i]==s2[i]:
                continue
            elif s1[i]==s2[i+2]:
                s2[i],s2[i+2]=s2[i+2],s2[i]
            elif s1[i+2]==s2[i]:
                s1[i],s1[i+2]=s1[i+2],s1[i]
            else:
                return False
        return s1==s2