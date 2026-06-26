class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        a=nums[0]
        count=1
        for i in nums[1:]:
            if nums.count(i)>count:
                a=i
                count=nums.count(i)
        return a