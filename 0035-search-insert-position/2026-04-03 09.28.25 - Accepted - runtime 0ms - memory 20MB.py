class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        low,high=0,len(nums)-1
        if target<nums[0]:
            return 0
        elif target>nums[high]:
            return high+1
        else:
            while low<=high:
                mid=(low+high)//2
                if nums[mid]==target:
                    return mid
                elif nums[mid]<target:
                    low=mid+1
                elif nums[mid]>target:
                    high=mid-1
            return low
