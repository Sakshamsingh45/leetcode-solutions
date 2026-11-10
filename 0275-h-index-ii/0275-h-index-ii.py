class Solution:
    def hIndex(self, citations: list[int]) -> int:
        low,high=0,len(citations)-1
        mx=0
        while low<=high:
            mid=(low+high)//2
            if citations[mid]>=len(citations)-mid:
                mx=max(mx,len(citations)-mid)
            if citations[mid]<len(citations)-mid:
                low=mid+1
            else:
                high=mid-1
        return mx