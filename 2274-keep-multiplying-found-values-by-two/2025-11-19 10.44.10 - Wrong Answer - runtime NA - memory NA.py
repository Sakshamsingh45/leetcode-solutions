class Solution:
    def findFinalValue(self, nums: List[int], original: int) -> int:
        max_original=0
        for i in nums:
            if i%original==0:
                original=i*2
            else:
                continue
        return original
