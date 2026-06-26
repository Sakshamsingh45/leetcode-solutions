class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        merg=[]
        i,j=0,0
        while i<len(nums1) or j<len(nums2):
            if nums1[i]==nums2[j]:
                merg.append(nums1)
                merg.append(nums2)i+=1
            j+=1
        elif nums1[i]<nums2[j]:
            merg.append(nums1[i])
            i+=1
        elif nums1[i]>nums2[j]:
            merg.append(nums2[j])
            j+=1
    while i < len(nums1):
        merg.append(nums1[i])
        i += 1

    while j < len(nums2):
        merg.append(nums2[j])
        j += 1
    
    a=len(merg)
    if a%2==0:
        return (merg[a//2]+merg[a//2+1])/2
    return merg[(a+1)//2]