class Solution:
    def firstStableIndex(self, nums: list[int], k: int) -> int:
        minst=float("inf")
        flag=True
        for i in range(len(nums)):
            no=max(nums[:i+1])-min(nums[i::])
            if no<=k and i<minst:
                minst=i
                flag=False
        if flag:
            return -1
        return minst