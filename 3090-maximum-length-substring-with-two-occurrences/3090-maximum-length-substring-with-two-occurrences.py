class Solution:
    def maximumLengthSubstring(self, s: str) -> int:
        mlen=0
        l=0
        freq={}
        for r in range(len(s)):
            if s[r] not in freq:
                freq[s[r]]=0
            freq[s[r]]+=1
            while freq[s[r]]>2:
                freq[s[l]]-=1
                l+=1
            mlen=max(mlen,r-l+1)
        return mlen