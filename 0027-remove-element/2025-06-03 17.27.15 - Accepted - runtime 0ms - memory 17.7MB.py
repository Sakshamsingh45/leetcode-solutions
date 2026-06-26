class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        b=0
        a=len(nums)
        count=-(len(nums))
        while count<0:
            if nums[count]==val:
                b+=1
                nums.pop(count)
            count+=1
            
        k=a-b
        return k