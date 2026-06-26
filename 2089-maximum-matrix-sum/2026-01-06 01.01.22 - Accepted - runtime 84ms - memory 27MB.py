class Solution:
    def maxMatrixSum(self, matrix: List[List[int]]) -> int:
        su=0
        count=0
        minarg=float("inf")
        for i in matrix:
            for j in i:
                if j<0:
                    count+=1
                minarg=min(minarg,abs(j))
                su+=abs(j)
        if count%2!=0:
            su-=2*minarg
        return su
