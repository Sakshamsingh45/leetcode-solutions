class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        nums.sort(key=lambda x:str(x)*10)
        ans=""
        for i in range(-1,-len(nums)-1,-1):
            ans+=str(nums[i])
        if ans[0]=="0":
            return "0"
        return ans