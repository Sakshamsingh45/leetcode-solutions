class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        a=0
        count=0
        for i in range (len(nums)):
            if nums.count(nums[i])>count:
                a=nums[i]
                count=nums.count(nums[i])
        return a