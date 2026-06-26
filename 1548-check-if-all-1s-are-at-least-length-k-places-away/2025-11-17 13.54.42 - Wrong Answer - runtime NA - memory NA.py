class Solution:
    def kLengthApart(self, nums: List[int], k: int) -> bool:
        i=0
        while i<len(nums)-1:
            zero=0
            if nums[i]==1 and nums[i+1]==0:
                i+=1
                while i<len(nums) and nums[i]!=1:
                    zero+=1
                    i+=1
                if i<len(nums) and zero<k:
                    return False
            else:
                i+=1
        return True

        