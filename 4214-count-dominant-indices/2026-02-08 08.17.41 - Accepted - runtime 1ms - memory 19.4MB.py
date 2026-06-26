class Solution:
    def dominantIndices(self, nums: List[int]) -> int:
        count=0
        n=len(nums)
        s=sum(nums)
        for i in range(n-1):
            s=s-nums[i]
            rlen=n-i-1
            if nums[i]>s/rlen:
                count+=1
        return count