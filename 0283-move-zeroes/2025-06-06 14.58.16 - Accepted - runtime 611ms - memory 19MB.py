class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        count=0
        a=len(nums)-1
        for i in nums:
            if count==a:
                break
            elif i ==0:
                nums.remove(0)
                nums.append(0)
            
        