class Solution:
    def longestAlternatingSubarray(self, nums: List[int], threshold: int) -> int:
        l=0
        mcount=0
        prev=1
        for r in range(len(nums)):
            if nums[l]%2==0 and nums[l]<=threshold:
                if prev!=nums[r]%2 and nums[r]<=threshold:
                    prev=nums[r]%2
                else:
                    l=r
            else:
                l+=1
                prev=0
            mcount=max(mcount,r-l+1)
        return mcount