class Solution:
    def maxSubsequence(self, nums: List[int], k: int) -> List[int]:
        sub=[]
        loop=1
        while loop<=k:
            a=max(nums)
            sub.append(a)
            nums.remove(a)
            loop+=1

        return sorted(sub)