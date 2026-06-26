class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        count=0
        for i in range(len(nums)):
            for j in range(i,len(nums)):
                cost=(max(nums[i:j+1])-min(nums[i:j+1]))*(j-i+1)
                if cost<=k:
                    count+=1
        return count