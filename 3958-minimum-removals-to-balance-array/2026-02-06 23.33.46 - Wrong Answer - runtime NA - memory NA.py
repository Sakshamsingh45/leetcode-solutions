class Solution:
    def minRemoval(self, nums: List[int], k: int) -> int:
        nums.sort()
        count=0
        mint=nums[0]
        while nums[-1]>mint*k:
            nums.pop()
            count+=1
        return count