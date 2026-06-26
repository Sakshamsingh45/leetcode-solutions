class Solution:
    def maxDistance(self, nums1: List[int], nums2: List[int]) -> int:
        dis=max(len(nums2),len(nums1))
        for i in range(len(nums1)):
            for j in range(len(nums2)-1,0,-1):
                if i<=j and nums1[i]<=nums2[j]:
                    return j-i
        return 0