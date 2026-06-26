class Solution:
    def maximumTripletValue(self, nums: List[int]) -> int:
        maxv=0
        for i in range (len(nums)):
            for j in range(i+1,len(nums)):
                for k in range (j+1,len(nums)):
                    value = (nums[i]-nums[j])*nums[k]
                    if value > maxv:
                        maxv=value
        return maxv
