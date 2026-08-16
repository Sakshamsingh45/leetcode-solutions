class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        l=0
        m=1
        count=0
        for r in range(len(nums)):
            m*=nums[r]
            while m>=k:
                if l>r:
                    break
                m//=nums[l]
                l+=1
            count+=(r-l+1)
        return count