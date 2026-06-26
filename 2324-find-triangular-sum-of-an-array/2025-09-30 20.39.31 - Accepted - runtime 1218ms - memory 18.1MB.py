
class Solution:
    def triangularSum(self, nums: List[int]) -> int:
        while len(nums) > 1:
            newnums = []
            for j in range(len(nums) - 1):
                newnums.append((nums[j] + nums[j + 1]) % 10)
            nums = newnums
        return nums[0]
