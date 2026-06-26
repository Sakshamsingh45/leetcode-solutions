class Solution:
    def kthSmallestProduct(self, nums1, nums2, k):
        products = []

        for num1 in nums1:
            for num2 in nums2:
                products.append(num1 * num2)

        products.sort()
        return products[k - 1]
