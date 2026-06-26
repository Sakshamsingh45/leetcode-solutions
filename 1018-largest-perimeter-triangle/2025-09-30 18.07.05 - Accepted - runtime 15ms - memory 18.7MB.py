class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        nums.sort()
        i=-1
        while i-2>=-len(nums):
            a=nums[i]
            b=nums[i-1]
            c=nums[i-2]
            if (a+b>c) and (a+c>b) and (b+c>a):
                return a+b+c
            else:
                i-=1
        return 0
