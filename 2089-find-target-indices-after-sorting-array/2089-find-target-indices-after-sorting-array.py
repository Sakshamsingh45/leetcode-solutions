class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        res=[]
        nums.sort()
        for idx,i in enumerate(nums):
            if i==target:
                res.append(idx)
        return res