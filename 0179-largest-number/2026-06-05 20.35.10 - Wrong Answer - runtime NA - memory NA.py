class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        nums.sort(key=lambda x:str(x)*10)
        ans=""
        for i in range(-1,-len(nums)-1,-1):
            ans+=str(nums[i])
        return ans