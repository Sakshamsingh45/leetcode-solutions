class Solution:
    def divideArray(self, nums: List[int]) -> bool:
        count = 0 
        b=set(nums)
        for i in b:
            count=nums.count(i)
            if count%2 != 0:
                return False
        return True

