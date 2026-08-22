class Solution:
    def largestInteger(self, nums: List[int], k: int) -> int:
        if k==len(nums):
            return max(nums)
        if len(nums)==0 or k>len(nums):
            return -1
        if len(nums)==1:
            return nums[0]
        else:
            freq={}
            for i in nums:
                freq[i]=freq.get(i,0)+1
            if k>1:
                if freq[nums[0]]==1 and freq[nums[-1]]==1:
                    return max(nums[0],nums[-1])
                elif freq[nums[0]]==1:
                    return nums[0]
                elif freq[nums[-1]]==1:
                    return nums[-1]
                else:
                    return -1
            else:
                mx=float("-inf")
                for i in nums:
                    if freq[i]==1:
                        mx=max(i,mx)
                return -1 if mx==float("-inf") else mx
        
        