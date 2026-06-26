class Solution:
    def maxDistance(self, nums1: List[int], nums2: List[int]) -> int:
        dis=-1
        for i in range(len(nums1)):
            for j in range(len(nums2)-1,0,-1):
                if i<=j and nums1[i]<=nums2[j]:
                    dis=max(dis,j-i)
        return 0 if dis==-1 else dis