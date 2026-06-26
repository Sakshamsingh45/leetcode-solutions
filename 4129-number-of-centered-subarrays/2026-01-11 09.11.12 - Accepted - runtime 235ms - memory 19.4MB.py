class Solution:
    def centeredSubarrays(self, nums: List[int]) -> int:
        count=0
        for i in range(len(nums)):
            count+=1
            temp=nums[i]
            seen=set()
            seen.add(nums[i])
            for j in range(i+1,len(nums)):
                temp+=nums[j]
                seen.add(nums[j])
                if temp in seen:
                    count+=1
                
        return count
                    
                
        
        