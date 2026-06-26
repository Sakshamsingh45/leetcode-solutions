class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        freq={}
        r=set()
        for i,j in enumerate(word):
            if j.islower() and j not in r:
                freq[j]=i
                if j.upper() in freq and freq[j.upper()]<freq[j]:
                    del freq[j]
                    del freq[j.upper()]
                    r.add(j)
                    r.add(j.upper())
            elif j.isupper() and j not in r:
                if j not in freq:
                    freq[j]=i
        count=0
        for k in freq:
            if k.islower() and k.upper() in freq:
                count+=1
        return count