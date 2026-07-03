class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        mg=[]
        i=j=0
        while i<len(nums1) and j<len(nums2):
            if nums1[i]<nums2[j]:
                mg.append(nums1[i])
                i+=1
            elif nums1[i]>nums2[j]:
                mg.append(nums2[j])
                j+=1
            else:
                mg.append(nums1[i])
                mg.append(nums2[j])
                i+=1
                j+=1
        while i<len(nums1):
            mg.append(nums1[i])
            i+=1
        while j<len(nums2):
            mg.append(nums2[j])
            j+=1
        l=len(mg)
        if l%2==0:
            return (mg[l//2]+mg[(l-1)//2])/2
        else:
            return float(mg[l//2])

