class Solution:
    def countGoodSubstrings(self, s: str) -> int:
        if len(s)<3:
            return 0
        freq={}
        l=0
        for i in range(3):
            freq[s[i]]=freq.get(s[i],0)+1
        count=1 if freq[s[0]]==1 and freq[s[1]]==1 and freq[s[2]]==1 else 0
        for r in range(3,len(s)):
            freq[s[l]]-=1
            freq[s[r]]=freq.get(s[r],0)+1
            l+=1
            if freq[s[l]]==1 and freq[s[l+1]]==1 and freq[s[l+2]]==1:
                count+=1
        return count
