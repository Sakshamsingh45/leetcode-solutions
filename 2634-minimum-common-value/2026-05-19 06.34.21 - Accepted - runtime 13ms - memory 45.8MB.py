class Solution:
    def getCommon(self, nums1: List[int], nums2: List[int]) -> int:
        ans=set(nums1).intersection(set(nums2))
        if ans:
            return min(ans)
        else:
            return -1