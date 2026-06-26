class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        intersection=[]
        nums1=set(nums1)
        for i in nums1:
            if i in nums2:
                intersection.append(i)
        return intersection
