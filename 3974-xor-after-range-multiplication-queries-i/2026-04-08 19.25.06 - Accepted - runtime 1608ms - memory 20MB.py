class Solution:
    def xorAfterQueries(self, nums: List[int], queries: List[List[int]]) -> int:
        
        MOD=(10**9)+7
        for i in queries:
            for j in range(i[0],i[1]+1,i[2]):
                nums[j]=(nums[j]*i[3])%(MOD)
        ans=nums[0]
        for k in range(1,len(nums)):
            ans=ans^nums[k]
        return ans