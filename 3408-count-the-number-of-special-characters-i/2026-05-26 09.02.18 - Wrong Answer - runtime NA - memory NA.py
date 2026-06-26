class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        count=0
        freq={}
        for i in word:
            if i.isupper():
                if i.lower() in freq and freq[i.lower()]>0:
                    count+=1
                    freq[i.lower()]-=1
                else:
                    freq[i]=1
            else:
                if i.upper() in freq and freq[i.upper()]>0:
                    count+=1
                    freq[i.upper()]-=1
                else:
                    freq[i]=1
        return count