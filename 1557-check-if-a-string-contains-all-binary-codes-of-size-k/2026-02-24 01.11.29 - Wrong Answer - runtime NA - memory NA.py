class Solution:
    def hasAllCodes(self, s: str, k: int) -> bool:
        k=bin(k)[2:]
        a=len(k)
        if len(s)<len(k):
            return False
        for i in range(len(s)-a):
            if k==s[i:i+a]:
                return True
        return False

                