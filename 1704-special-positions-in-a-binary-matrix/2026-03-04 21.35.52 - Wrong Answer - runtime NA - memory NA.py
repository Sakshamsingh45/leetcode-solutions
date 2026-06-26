class Solution:
    def numSpecial(self, mat: List[List[int]]) -> int:
        count=0
        s=set()
        for i in range(len(mat)):
            flag=True
            for j in range(len(mat[i])):
                if j in s:
                    continue
                if mat[i][j]==1:
                    s.add(j)
                    flag=True
                    for k in range(len(mat)):
                        if k==i:
                            continue
                        if mat[k][j]==1:
                            flag=False
                            break
                    if flag:
                        count+=1
        return count


                