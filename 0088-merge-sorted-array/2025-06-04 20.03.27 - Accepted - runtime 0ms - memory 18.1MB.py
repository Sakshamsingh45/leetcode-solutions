from typing import List

class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        b = [] 
        i = 0
        j = 0
        while i < m and j < n:
            if nums1[i] < nums2[j]:
                b.append(nums1[i])
                i += 1
            elif nums1[i] == nums2[j]:
                b.append(nums1[i])
                b.append(nums2[j])
                i += 1
                j += 1
            else:
                b.append(nums2[j])
                j += 1

        while i < m:
            b.append(nums1[i])
            i += 1

        while j < n:
            b.append(nums2[j])
            j += 1

        for x in range(m + n):
            nums1[x] = b[x]
