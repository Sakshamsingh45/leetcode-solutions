class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        min1=0
        for i in triangle :
            min1+=min(i)
        return min1