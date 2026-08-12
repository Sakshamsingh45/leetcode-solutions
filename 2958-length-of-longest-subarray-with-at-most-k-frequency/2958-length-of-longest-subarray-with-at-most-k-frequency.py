class Solution:
    def maxSubarrayLength(self, nums: List[int], k: int) -> int:
        freq={}
        mlen=0
        l=0
        for idx,r in enumerate(nums):
            if r not in freq:
                freq[r]=0
            freq[r]+=1
            while freq[r]>k:
                freq[nums[l]]-=1
                l+=1
            mlen=max(mlen,idx-l+1)
        return mlen