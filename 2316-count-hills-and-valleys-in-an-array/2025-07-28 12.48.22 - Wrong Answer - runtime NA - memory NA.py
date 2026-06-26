class Solution:
    def countHillValley(self, nums: List[int]) -> int:
        count=-1
        for i in range(1,len(nums)-1):
            left=i-1
            right=i+1
            while left>-1 and nums[left]==nums[i]:
                left-=1
            while nums[right]==nums[i] and right<len(nums)+1:
                right+=1
            if nums[left]==nums[i] or nums[right]==nums[i]:
                continue
            else:
                if ( nums[i]>nums[right] and nums[i]>nums[left] ) or (nums[i]<nums[left] and nums[i]<nums[right]):
                    count+=1


        return count