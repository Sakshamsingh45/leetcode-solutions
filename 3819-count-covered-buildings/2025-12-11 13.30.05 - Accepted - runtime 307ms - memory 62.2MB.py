from typing import List

class Solution:
    def countCoveredBuildings(self, n: int, buildings: List[List[int]]) -> int:
        count = 0
        xmax, xmin, ymax, ymin = {}, {}, {}, {}
        for x, y in buildings:
            if x in xmax:
                if y > xmax[x]:
                    xmax[x] = y
                if y < xmin[x]:
                    xmin[x] = y
            else:
                xmax[x] = y
                xmin[x] = y
            if y in ymax:
                if x > ymax[y]:
                    ymax[y] = x
                if x < ymin[y]:
                    ymin[y] = x
            else:
                ymax[y] = x
                ymin[y] = x
        for x, y in buildings:
            if xmin[x] < y < xmax[x] and ymin[y] < x < ymax[y]:
                count += 1

        return count