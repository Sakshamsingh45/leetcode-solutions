class Solution:
    def largestMagicSquare(self, grid: List[List[int]]) -> int:
        def check(l, t, y):
            r = {}
            c = {}
            d1 = d2 = 0
            for q in range(y):
                for w in range(y):
                    if q == w:
                        d1+=grid[l+q][t+w]
                    if q + w == y - 1:
                        d2+=grid[l+q][t+w]
                    r[q] = r.get(q, 0) + grid[l+q][t+w]
                    c[w] = c.get(w, 0) + grid[l+q][t+w]
            target=r[0]
            for z in range(len(c)):
                if c[z] == target and  r[z]==target:
                    continue
                else:
                    return False
            if d2==target and d1==target:
                return True
            return False

        column, row = len(grid[0]), len(grid)
        mins = min(column, row)
        ri, cj = 0, 0
        while mins > 1:
            if check(ri, cj, mins):
                return mins
            if ri + mins < row:
                ri += 1
            else:
                if cj + mins < column:
                    cj += 1
                    ri = 0
                else:
                    mins -= 1
                    ri, cj = 0, 0
        return mins
