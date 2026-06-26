
class Solution:
    def triangularSum(self, nums: List[int]) -> int:
        i = len(nums)
        while i != 1:
            j = 0
            newnums = []
            while j != len(nums) - 1:
                newnums.append((nums[j] + nums[j + 1]) % 10)
                j += 1
            nums = newnums
            i = len(nums)
        return nums[0]
