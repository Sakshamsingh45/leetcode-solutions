class Solution:
    def minMirrorPairDistance(self, nums: List[int]) -> int:
        prev=dict()
        ans=inf
        for i,val in enumerate(nums):
            if val in prev:
                ans=min(ans,i-prev[val])
            prev[int(str(val)[::-1])]=i
        return -1 if ans==inf else ans