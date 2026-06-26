class Solution:
    def kthSmallestProduct(self, nums1, nums2, k):
        def count_less_equal(x):
            # Count number of products <= x
            count = 0
            for a in nums1:
                if a > 0:
                    # For positive a, find max b such that a * b <= x
                    l, r = 0, len(nums2)
                    while l < r:
                        m = (l + r) // 2
                        if a * nums2[m] <= x:
                            l = m + 1
                        else:
                            r = m
                    count += l
                elif a < 0:
                    # For negative a, find min b such that a * b <= x
                    l, r = 0, len(nums2)
                    while l < r:
                        m = (l + r) // 2
                        if a * nums2[m] <= x:
                            r = m
                        else:
                            l = m + 1
                    count += len(nums2) - l
                else:  # a == 0
                    if x >= 0:
                        count += len(nums2)
            return count

        nums2.sort()  # Ensure nums2 is sorted
        left, right = -10**10, 10**10

        while left < right:
            mid = (left + right) // 2
            if count_less_equal(mid) < k:
                left = mid + 1
            else:
                right = mid

        return left
