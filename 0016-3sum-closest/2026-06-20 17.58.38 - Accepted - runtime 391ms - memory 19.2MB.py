class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        close=sum(nums[:3])
        for i in range(len(nums)):
            st,lt=i+1,len(nums)-1
            while st<lt:
                n=nums[i]+nums[st]+nums[lt]
                if abs(target-n)<abs(target-close):
                    close=n
                if n<target:
                    st+=1
                elif n>target:
                    lt-=1
                else:
                    return target
        return close
                