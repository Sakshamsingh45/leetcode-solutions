class Solution:
    def maxDistance(self, nums1: List[int], nums2: List[int]) -> int:
        i=0
        dis=0
        while i<len(nums1):
            for j in range(i,len(nums2)):
                if nums1[i] <= nums2[j]:
                    dis=max(dis,j-i)
            i+=1
        return dis