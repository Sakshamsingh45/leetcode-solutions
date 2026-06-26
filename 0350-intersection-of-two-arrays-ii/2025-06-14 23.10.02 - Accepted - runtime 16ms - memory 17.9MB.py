class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        inter=[]
        a=set(nums1)
        b=set(nums2)
        c=a & b
        for i in c:
            for j in range(min(nums1.count(i),nums2.count(i))):
                inter.append(i)
        return inter
