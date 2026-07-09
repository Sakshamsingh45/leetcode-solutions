class Solution:
    def findLHS(self, nums):
        freq={}
        for i in nums:
            freq[i]=freq.get(i,0)+1
        maxlen=0
        for i in freq:
            if i+1 in freq:
                length=freq[i]+freq[i+1]
                maxlen=max(maxlen,length)
        return maxlen