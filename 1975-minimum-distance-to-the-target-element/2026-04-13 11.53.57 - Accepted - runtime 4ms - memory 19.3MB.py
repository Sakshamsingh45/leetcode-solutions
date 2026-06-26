class Solution:
    def getMinDistance(self, nums: List[int], target: int, start: int) -> int:
        minn=float("inf")
        for y,i in enumerate(nums):
            if i==target and abs(start-y)<minn:
                minn=abs(start-y)
        return minn            