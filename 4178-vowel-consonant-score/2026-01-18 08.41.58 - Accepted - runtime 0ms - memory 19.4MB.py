class Solution:
    def vowelConsonantScore(self, s: str) -> int:
        v=0
        c=0
        a={"a","e","i","o","u"}
        for i in s:
            if i in a:
                v+=1
            elif i.isalpha():
                c+=1
        return 0 if c==0 else v//c
                