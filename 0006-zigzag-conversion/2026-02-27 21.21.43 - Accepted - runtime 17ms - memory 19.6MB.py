class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s
        a = [[] for _ in range(numRows)]
        count = 0
        dir=1
        for i in s:
            a[count].append(i)
            if count==0:
                dir=1
            elif count==numRows-1:
                dir=-1
            count+=dir
        b = ""
        for i in a:
            b += "".join(i)
        return b