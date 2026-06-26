class Solution:
    def minimumCost(self, nums: List[int]) -> int:
        mincost=nums[0]
        nums=nums[1:]
        nums.sort()
        mincost+=nums[0]+nums[1]
        return mincost
