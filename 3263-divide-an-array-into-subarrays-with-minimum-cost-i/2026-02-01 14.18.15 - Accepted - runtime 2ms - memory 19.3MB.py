class Solution:
    def minimumCost(self, nums: List[int]) -> int:
        mincost=nums[0]
        nums.remove(mincost)
        nums.sort()
        mincost+=nums[0]+nums[1]
        return mincost
