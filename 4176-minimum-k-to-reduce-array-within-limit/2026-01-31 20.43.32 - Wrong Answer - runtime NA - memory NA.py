class Solution:
    def minimumK(self, nums: List[int]) -> int:
        l=max(nums)
        for i in range(1,l+1):
            op=0
            for j in nums:
                op+=(j+i-1)//i
                if op>i**2:
                    break
            if op<=i**2:
                return i
            
                
            
            