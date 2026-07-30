class Solution:
    def minimumPushes(self, word: str) -> int:
        i=0
        count=0
        s=0
        while i<len(word):
            if i%8==0:
                s+=1
            count+=s
            i+=1
        return count