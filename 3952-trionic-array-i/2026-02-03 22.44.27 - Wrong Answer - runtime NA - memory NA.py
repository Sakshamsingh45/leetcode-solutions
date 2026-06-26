class Solution:
    def isTrionic(self, nums: List[int]) -> bool:
        prev=float("-inf")
        count=0
        for i in range(len(nums)):
            if nums[i]>prev:
                prev=nums[i]
                continue
            else:
                count+=1
                for j in range(i+1,len(nums)):
                    if nums[i]<prev:
                        prev=nums[i]
                        continue
                    else:
                        count+=1
                        for k in range(j+1,len(nums)):
                            if nums[i]>prev:
                                prev=nums[i]
                            else:
                                return False
                        return True if count==2 else False
                    return False
            return False
