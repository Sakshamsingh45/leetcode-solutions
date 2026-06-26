class Solution:
    def prefixesDivBy5(self, nums: List[int]) -> List[bool]:
        number=0
        for i in range(len(nums)):
            number=2*number+nums[i]
            if number%5==0:
                nums[i]=True
            else:
                nums[i]=False
        return nums
        