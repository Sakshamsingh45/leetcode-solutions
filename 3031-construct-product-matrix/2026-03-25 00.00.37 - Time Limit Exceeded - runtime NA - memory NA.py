class Solution:
    def constructProductMatrix(self, grid: List[List[int]]) -> List[List[int]]:
        product=1
        MOD=12345
        for i in grid:
            for j in i:
                product*=j
        p=[[0 for j in range(len(grid[0]))] for i in range(len(grid))]
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                p[i][j]=(product//grid[i][j])%MOD
        return p

