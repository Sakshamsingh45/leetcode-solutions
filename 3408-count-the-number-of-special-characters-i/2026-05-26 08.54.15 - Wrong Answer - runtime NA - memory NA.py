class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        count=0
        freq={}
        for i in word:
            if i.isupper():
                if i.lower() in freq:
                    count+=1
                else:
                    freq[i]=1
            else:
                if i.upper() in freq:
                    count+=1
                else:
                    freq[i]=1
        return count