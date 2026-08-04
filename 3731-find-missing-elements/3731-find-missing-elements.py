class Solution:
    def findMissingElements(self, nums: List[int]) -> List[int]:
        nums.sort()
        res=[]
        prev=nums[0]-1
        for i in nums:
            if i==prev+1:
                prev+=1
                continue
            else:
                while prev+1!=i:
                    res.append(prev+1)
                    prev+=1
            prev=i
        return res