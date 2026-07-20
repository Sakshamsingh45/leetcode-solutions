class Solution:
    def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        row, col = len(grid), len(grid[0])

        # Flatten the grid
        gd = []
        for i in range(row):
            for j in range(col):
                gd.append(grid[i][j])

        # Shift
        n = len(gd)
        k %= n
        gd = gd[-k:] + gd[:-k]

        # Put values back
        count = 0
        for i in range(row):
            for j in range(col):
                grid[i][j] = gd[count]
                count += 1

        return grid