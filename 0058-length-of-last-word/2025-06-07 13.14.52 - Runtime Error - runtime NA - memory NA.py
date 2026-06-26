class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        a=-1
        count=0
        s=s.rstrip()
        while True:
            if s[a]==" ":
                break
            else:
                count+=1
                a-=1
        return count

