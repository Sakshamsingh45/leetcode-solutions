class Solution:
    def scoreDifference(self, nums: List[int]) -> int:
        firsts=0
        seconds=0
        first=True
        second=False
        for i in range(len(nums)):
            if nums[i]&1!=0:
                first,second=second,first
            if (i+1)%6==0:
                first,second=second,first
            if first:
                firsts+=nums[i]
            if second:
                seconds+=nums[i]
        return firsts-seconds
            