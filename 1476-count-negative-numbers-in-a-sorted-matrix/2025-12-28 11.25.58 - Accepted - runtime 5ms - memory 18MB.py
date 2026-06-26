class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        i=-1
        limit,count=-len(grid[0]),0
        while i>=-len(grid):
            if limit>=0:
                return count
            j=-1
            while j>=limit:
                if grid[i][j]>=0:
                    limit=j-1
                    break
                count+=1
                j-=1
            i-=1
        return count

        