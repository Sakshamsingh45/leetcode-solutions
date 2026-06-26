class Solution:
    def reverseSubmatrix(self, grid: List[List[int]], x: int, y: int, k: int) -> List[List[int]]:
        if x+k>len(grid) or y+k>len(grid[0]):
            return False
        count=k-1
        for i in range(x,x+k//2):
            for j in range(y,y+k):
                temp=grid[i][j]
                grid[i][j]=grid[i+count][j]
                grid[i+count][j]=temp
            count-=2
        return grid