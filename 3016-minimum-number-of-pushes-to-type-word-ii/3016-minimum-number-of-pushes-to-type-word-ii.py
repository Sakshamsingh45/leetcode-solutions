class Solution:
    def minimumPushes(self, word: str) -> int:
        freq={}
        for i in word:
            if i not in freq:
                freq[i]=0
            freq[i]+=1
        tup=[]
        for i in freq:
            tup.append((i,freq[i]))
        tup.sort(key=lambda x:x[1],reverse=True)
        count=0
        s=0
        for i,j in enumerate(tup):
            if i%8==0:
                count+=1
            s+=(count*j[1])
        return s
