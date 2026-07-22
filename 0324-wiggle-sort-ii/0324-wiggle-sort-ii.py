class Solution:
    def wiggleSort(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        nums.sort()
        n=len(nums)
        res=[]
        mid=n//2 if n%2==0 else (n+1)//2
        st,lst=mid-1,n-1
        dir=True
        while 0<=st or lst>=mid:
            if dir:
                res.append(nums[st])
                dir=False
                st-=1
            else:
                res.append(nums[lst])
                dir=True
                lst-=1
        nums[:]=res[:]

