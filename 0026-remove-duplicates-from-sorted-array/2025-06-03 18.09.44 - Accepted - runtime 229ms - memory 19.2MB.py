class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        a=0
        while a<len(nums):
            c=a+1
            while c<len(nums):
                if nums[c]==nums[a]:
                    nums.pop(c)
                else:
                    c+=1
            a+=1
        k= len(nums)
        return k
        