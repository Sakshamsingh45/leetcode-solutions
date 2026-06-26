class Solution:
    def minOperations(self, grid: List[List[int]], x: int) -> int:
        result=0
        l=[]
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                l.append(grid[i][j])
        l.sort()
        m=l[len(l)//2]
        for k in l:
            if k%x==m%x:
                result += abs(k-m) // x
            else:
                return -1
        return result