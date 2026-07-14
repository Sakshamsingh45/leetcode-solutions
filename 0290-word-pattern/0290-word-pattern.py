class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        s=s.split(" ")
        if len(s)!=len(pattern):
            return False
        freq={}
        for i in range(len(s)):
            if ("W",s[i]) in freq and freq[("W",s[i])]!=pattern[i]:
                return False
            if ("P",pattern[i]) in freq and freq[("P",pattern[i])]!=s[i]:
                return False
            freq[("W",s[i])]=pattern[i]
            freq[("P",pattern[i])]=s[i]
        return True
