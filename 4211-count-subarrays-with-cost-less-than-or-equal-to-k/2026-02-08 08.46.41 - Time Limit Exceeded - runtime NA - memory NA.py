class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        count=0
        for i in range(len(nums)):
            curmin=nums[i]
            curmax=nums[i]
            for j in range(i,len(nums)):
                curmin=min(curmin,nums[j])
                curmax=max(curmax,nums[j])
                cost=(curmax-curmin)*(j-i+1)
                if cost<=k:
                    count+=1
        return count