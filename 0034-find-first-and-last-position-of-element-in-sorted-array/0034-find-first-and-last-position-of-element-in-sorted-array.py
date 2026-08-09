class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        l,r=0,len(nums)-1
        while l<=r:
            mid=(l+r)//2
            if nums[mid]==target:
                left=right=mid
                ll,rr=0,mid-1
                while ll<=rr:
                    m=(ll+rr)//2
                    if nums[m]==target:
                        left=m
                        rr=m-1
                    elif nums[m]<target:
                        ll=m+1
                    else:
                        rr=m-1
                ll,rr=mid+1,len(nums)-1
                while ll<=rr:
                    m=(ll+rr)//2
                    if nums[m]==target:
                        right=m
                        ll=m+1
                    elif nums[m]>target:
                        rr=m-1
                    else:
                        ll=m+1

                return [left,right]
            elif nums[mid]<target:
                l=mid+1
            else:
                r=mid-1
        return [-1,-1]
                