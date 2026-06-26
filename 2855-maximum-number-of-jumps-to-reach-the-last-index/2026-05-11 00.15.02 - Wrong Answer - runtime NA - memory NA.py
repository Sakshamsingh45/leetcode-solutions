class Solution:
    def maximumJumps(self, nums: List[int], target: int) -> int:
        count=i=0
        while i<len(nums)-1:
            flag=True
            for j in range(i+1,len(nums)):
                if abs(nums[j]-nums[i])<=target:
                    i=j
                    flag=False
                    count+=1
                    break
            if flag :
                return -1
        return count
